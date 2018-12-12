import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myveryowncookbook'
app.config["MONGO_URI"] = 'mongodb://admin:Vonnegut28@ds227654.mlab.com:27654/myveryowncookbook'

mongo = PyMongo(app)

@app.route('/')

@app.route('/add_user')
def add_user():
    return render_template("user_registration.html")

@app.route('/insert_user', methods=['POST'])
def insert_user():
    users = mongo.db.users
    users.insert_one(request.form.to_dict())
    return redirect(url_for("entry"))
    
@app.route('/entry')
def entry():
    return render_template("entry.html")

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
    categories=mongo.db.categories.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())
    
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
          port=int(os.environ.get('PORT')),
          debug=True)