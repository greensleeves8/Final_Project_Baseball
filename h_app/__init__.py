from flask import Flask
from flask import render_template

app_h = Flask(__name__)

@app_h.route('/Baseball')
def Baseball():
    return "<h1> Baseball Hall of Fame </h1>"

@app_h.route('/')
def home():
    return render_template("index.html")