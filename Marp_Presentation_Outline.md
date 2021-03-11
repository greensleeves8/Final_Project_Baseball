---
marp: true
theme: base
#class: invert
---
# Machine Learning and the Hall of Fame
Cale Green, Camille Goodwin, Claire Davis, Matt Martin, Silas Cobb, Trey Wehrmeyer 


---


<style>
section {
  background: #B0C4DE;
}
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

# Overview 
- Proposal
- Resources
- Technologies Used
- Process (ETL, Database, Machine Learning, Visualizations, Deployment & Heroku)
- Web App - Live Demo
- Pitch & Selling Points
- Future Advancements


---
# Proposal 
## Using machine learning to predict future members to the Baseball Hall of Fame

- Predict future inductees
- Examine the statistically-worthy players who have not yet been inducted
- Recognize historically underrated players

---
# Resources

*[Sean Lahman's Baseball Databse](http://www.seanlahman.com/baseball-archive/statistics/)*

*[Baseball Reference](https://www.baseball-reference.com/)*

*[Baseball Hall](https://baseballhall.org/)*

*[Fangraphs](https://www.fangraphs.com/)*

Tables Used:
- Pitching.csv
- Batting.csv
- HallOfFame.csv

[For additional information and resources: Click Here!](https://github.com/greensleeves8/Final_Project_Baseball)

---
# Technologies Used

- Python and Pandas for data exploration and ETL
- PostgreSQL for a database
- Extreme Gradient Boosting machine learning model
- Matplotlib for visualization of findings
- Heroku, Flask, HTML, and JavaScript for dashboard creation and deployment
  
---
# ETL
### Batting ETL:
Created Career_Batting_df by:
- Merging Batting and Hall of Fame CSV's
- Dropping columns with too many null values
- Adding some necessary calculated statistics 
### Pitching ETL:
Created Career_Pitching_df by:
- Merging the pitching and Hall of Fame CSV's
- Dropping players who did not meet the minimum time to be eligible for the HOF
- Additional necessary calculated columns were added


---
### Final Hall Batter Dataframe in Jupyter Notebook
![](Images/ETL_Image.JPG)

---
# Database
- Create connection to database from ETL documents
- Import 4 tables to PostgreSQL
- Pull tables from Postgres to machine learning documents with cursor object

---
### Entity Relationship Diagram
 ![center](Images/ERD.JPG)


---
# Live Demo

https://hall-of-fame-baseball.herokuapp.com/

---
# Machine Learning Model

- Targeted models with high recall scores
  - Finding eligible players from so many ineligible
- Secondary priority, precision scores 
  - If predicted in HOF, how likely is it true

---

![bg left](https://github.com/greensleeves8/Final_Project_Baseball/blob/main/Machine_Learning_Models/Viz_Resources/Batting_Feature_Importances.png)

![bg](https://github.com/greensleeves8/Final_Project_Baseball/blob/main/Machine_Learning_Models/Viz_Resources/Batting_Corr.pdf)

---

## Comparison of Tested Models
| Model and Sampling Method | Accuracy | Yes/No |Precision | Recall | F-1 Score |
| --------------- | -------- | ------ |--------- | ------ | --------- |
| *XGBoost Classifier with SMOTE* | 98.9% | *No* | 1.00 | 0.99 | 0.99 |
| | | *Yes* | 0.46 | 0.77 | 0.58 |
| | | | | | |
| *Random Forest Classifier (RFC)* | 99.2% | *No* | 0.99 | 1.00 | 1.00 |
| | | *Yes* | 0.63 | 0.44 | 0.52 |
| | | | | | |
| *RFC with SMOTE* | 98.5% | *No* | 1.00 | 0.99 | 0.99 |
| | | *Yes* | 0.31 | 0.76 | 0.44 |
| | | | | | |
| *Logistic Regression* | 99.4% | *No* | 1.00 | 1.00 | 1.00 |
| | | *Yes* | 0.59 | 0.56 | 0.58 |
| | | | | | |
| *Logistic Regression with 75% Threshold* | 99.4% | *No* | 0.99 | 1.00 | 1.00 |
| | | *Yes* | 0.71 | 0.35 | 0.47 |
| | | | | | |

---

![bg contain](https://github.com/greensleeves8/Final_Project_Baseball/blob/main/Machine_Learning_Models/Viz_Resources/Batter_HOF_2022_Results.png)

---

# Deployment and Heroku
- Used HTML, CSS, Boostrap, JS, Python, and Flask to build dynamic webpage
- Ability to scrape HOF website top article and pictures
- Set up file system according to Heroku's speicifcations to deploy our project
  - h_app, html files, Procfile, requirements, wsgi

---
### Code to Filter Interactive Table
![center](Images/js_filtering.jpg)

---
# Pitch & Selling Points
- Tool for fans and professionals to evaluate players' Hall of Fame case based solely on their on-field production, with a high degree of accuracy
- Sell to baseball teams for drafting players or Hall of Fame electors 
- Takes bias out of the process
- Easy to update and run year after year

---
# Future Advancements
- Expand to other sports, awards, 
- Predict all star teams
- Prediction table to display odds of players being inducted
- Work on style CSS to be more user friendly and clean

---
# Thank you for your attention.
# Any questions or concerns? 