from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import hof_scraping
import datetime as dt
import os

app_h = Flask(__name__)

app_h.config["MONGO_URI"] = os.environ['APP_SETTINGS']
mongo = PyMongo(app_h)


@app_h.route('/')
def home():
    hall = mongo.db.hall.find_one()
    return render_template("index.html", hall=hall)

@app_h.route('/Background Knowledge')
def Baseball():
    return render_template("background.html")

# Create a scraping route 

@app_h.route("/scrape")
def scrape():
    hall = mongo.db.hall
    hall_data = hof_scraping.scrape_all()
    hall.update({}, hall_data, upsert=True)

    return redirect('scrape.html', code=302)


if __name__ == "__main__":
    app_h.run(debug=True)