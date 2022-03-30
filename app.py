# IMPORT TOOLS
# use Flask to render a template, redirecting to another url, and creating a URL.
from flask import Flask, render_template, redirect, url_for
# use PyMongo to interact with our Mongo database.
from flask_pymongo import PyMongo
# use the scraping code that will be converted from .ipynb file to .py file.
import scraping

# set up Flask
app = Flask(__name__)

# tell Python how to connect to Mongo using PyMongo:
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# define the route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# set up the scraping route.
   @app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

# tell Flask to run.
if __name__ == "__main__":
   app.run()