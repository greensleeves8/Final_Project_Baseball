from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import hof_scraping
import datetime as dt
import os

app_h = Flask(__name__)


app_h.config["MONGO_URI"] = os.environ['APP_SETTINGS']
print(app_h.config["MONGO_URI"])
try: 
    mongo = PyMongo(app_h)
except: 
    print("Did not run")
    print(app_h.config["MONGO_URI"])


@app_h.route('/')
def home():
    return render_template("index.html")


@app_h.route('/Background')
def Baseball():
    return render_template("background.html")


@app_h.route('/Batting')
def Batting():
    return render_template("batting.html")


@app_h.route('/Pitching')
def Pitching():
    return render_template("pitching.html")


@app_h.route('/Prediction')
def Prediction():
    return render_template("prediction.html")

# Create a scraping route 

@app_h.route("/scrape")
def scrape():
    hall_db = mongo.db.hall
    hall_data = hof_scraping.scrape_all()
    hall_db.update({}, hall_data, upsert=True)
    hall = hall_db.find()
    
    return render_template("scrape.html", hall=hall)


if __name__ == "__main__":
    app_h.run(debug=True)