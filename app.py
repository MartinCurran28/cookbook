import os
import json
from flask import Flask, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import MongoClient

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myveryowncookbook'
app.config["MONGO_URI"] = 'mongodb://admin:Vonnegut28@ds227654.mlab.com:27654/myveryowncookbook'

mongo = PyMongo(app)

@app.route('/')
    
@app.route('/get_categories')
def get_categories():
    return render_template("categories.html")
    
@app.route('/user')
def user():
    return render_template('login.html')

@app.route('/login', methods=["GET","POST"])
def login():
    users = mongo.db.users
    client = users.find_one({'username' : request.form['username']})

    if client:
        session['username'] = request.form['username']
        return redirect(url_for('get_categories'))
    else:    
        return  "not a valid username"
        
@app.route('/register')
def register():
    return render_template("registration.html",
    users=mongo.db.users.find())

@app.route('/user_info', methods=['POST'])
def user_info():
    users =  mongo.db.users
    users.insert_one(request.form.to_dict())
    return redirect(url_for('user'))
    
    
@app.route('/get_breakfast')
def get_breakfast():
    return render_template('breakfast.html',
    recipes = mongo.db.recipes.find())

@app.route('/get_lunch')
def get_lunch():
    return render_template("lunch.html",
    recipes = mongo.db.recipes.find()) 
    
@app.route('/get_dinner')
def get_dinner():
    return render_template("dinner.html",
    recipes = mongo.db.recipes.find())    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
    categories=mongo.db.categories.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_categories'))
    
    
@app.route('/graphs')
def graphs():
    return render_template('graphs.html')
    
@app.route("/recipes/data")
def recipes():
    FIELDS = {
        '_id': False, 'recipe_name': True, 'ingredients': True,
        'calories': True, 'recipe_author': True, 'cuisine':True,
        'category_name': True
    }
    with MongoClient('mongodb://admin:Vonnegut28@ds227654.mlab.com:27654/myveryowncookbook') as conn:
        collection = conn['myveryowncookbook']['recipes']
        projects = collection.find(projection=FIELDS)
        return json.dumps(list(projects))


    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({"_id": ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get['recipe_name'],
        'category_name':request.form.get['category_name'],
        'ingredients': request.form.get['ingredients'],
        'directions': request.form.get['directions'],
        'prep_time':request.form.get['prep_time'],
        'cooking_time':request.form.get['cooking_time']
        
    })
    return redirect(url_for('get_categories'))
    
 
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('get_categories'))
    

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('view_recipe.html', recipe=the_recipe, categories=all_categories)
    
if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
          port=int(os.environ.get('PORT')),
          debug=True)