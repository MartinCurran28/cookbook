import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myveryowncookbook'
app.config["MONGO_URI"] = 'mongodb://admin:Vonnegut28@ds227654.mlab.com:27654/myveryowncookbook'

mongo = PyMongo(app)

@app.route('/')


@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html")
    
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html",
    recipes=mongo.db.recipes.find())
    
    
    
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
          port=int(os.environ.get('PORT')),
          debug=True)
    