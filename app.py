# Import our tools
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import hof_scraping

app = Flask(__name__)
app.debug = True

# Use pymongo to set up mongo conection


app.config["MONGO_URI"] = "mongodb://localhost:27017/halldb"
mongo = PyMongo(app)

# Seting up home route


@app.route("/")
def index():
    hall = mongo.db.hall.find_one()
    return render_template("index.html", hall=hall)


# Create a scraping route (connect it to button?)


@app.route("/scrape")
def scrape():
    hall = mongo.db.hall
    hall_data = hof_scraping.scrape_all()
    hall.update({}, hall_data, upsert=True)

    return redirect('/', code=302)


if __name__ == "__main__":
    app.run()
