# Import our dependencies
import pandas as pd
import xgboost as xgb
import joblib
from xgboost.sklearn import XGBClassifier
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from pathlib import Path
from imblearn.over_sampling import SMOTE

import psycopg2
from config import db_password

# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

conn = psycopg2.connect(host="localhost", port = 5432, database="baseball_data", user="postgres", password=db_password)

# Create a cursor object
cur = conn.cursor()

# A sample query of all data from the "career_batter" table in the "baseball_data" database
cur.execute("""SELECT * FROM career_batter LIMIT 5""")
query_results = cur.fetchall()
print(query_results)

# import entire career_batter table from postgres to dataframe
career_batter = pd.read_sql('SELECT * FROM career_batter', conn)
career_batter

# import entire hall_batter table from postgres to dataframe
hall_batter = pd.read_sql('SELECT * FROM hall_batter', conn)
hall_batter

cur.close()
conn.close()

# ML model data preprocessing
# Convert inducted column to Y = 1, N = 0

b = {'Y': 1, 'N': 0}
hall_batter['inducted'] = hall_batter['inducted'].map(b).fillna(hall_batter['inducted'])
hall_batter

# Set target and features variables
y = hall_batter.inducted
X = hall_batter.drop(columns=["playerID", "inducted"])

# Split training/test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42)

#Scale the data
#Create a StandardScaler instance
scaler = StandardScaler()

# Fit the StandardScaler
X_scaler = scaler.fit(X_train)

# Scale data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

# Use SMOTE to addres imbalanced dataset
X_resampled, y_resampled = SMOTE(random_state=42,
sampling_strategy='auto').fit_resample(
   X_train_scaled, y_train)

# Create a XGB model
XGB_model = XGBClassifier(max_depth = 5, min_child_weight = 1, gamma = 0, subsample = 0.8, colsample_bytree = 0.8, scale_pos_weight = 1, use_label_encoder = False)

# Fit the model
XGB_model = XGB_model.fit(X_resampled, y_resampled)

print(XGB_model)

# Use model to generate predictions
predictions = XGB_model.predict(X_test_scaled)

predictions

# Evaluate the model

# Calculating the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Create a DataFrame from the confusion matrix.
cm_df = pd.DataFrame(cm, index= ["Actual 0", "Actual 1"], columns = ["Predicted 0", "Predicted 1"])

# Calculate the accuracy score
acc_score = accuracy_score(y_test, predictions)

# Display results
print("Confustion Matrix")
display(cm_df)
print(f"Accuracy Score : {acc_score}")
print("Classification Report")
print(classification_report(y_test, predictions))

# Calculate feature importance in the XGB model
importances = XGB_model.feature_importances_
importances

# Sort the features by their importance
sorted(zip(XGB_model.feature_importances_, X.columns), reverse=True)

# Save the Model
filename = 'Final_XGB_Batter_Model.sav'
joblib.dump(XGB_model, filename)