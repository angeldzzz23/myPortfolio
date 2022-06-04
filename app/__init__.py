import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/home')
def home():
    return render_template('home.html', title="hey", url=os.getenv("URL"))

@app.route("/about")
def about():
    return render_template("about.html", title="About Lorem", url=os.getenv("URL"))