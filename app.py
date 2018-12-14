import os
from flask import Flask, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myveryowncookbook'
app.config["MONGO_URI"] = 'mongodb://admin:Vonnegut28@ds227654.mlab.com:27654/myveryowncookbook'

mongo = PyMongo(app)

@app.route('/')

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
    categories=mongo.db.categories.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {"_id": ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get['recipe_name'],
        'category_name':request.form.get['category_name'],
        'ingredients': request.form.get['ingredients'],
        'directions': request.form.get['directions'],
        'prep_time':request.form.get['prep_time'],
        'cooking_time':request.form.get['cooking_time']
    })
    return redirect(url_for('get_recipes'))
    

@app.route('/add_user')
def add_user():
    return render_template("user_registration.html")
    

@app.route('/insert_user', methods=['POST', 'GET'])
def insert_user():
    users = mongo.db.users
    users.insert_one(request.form.to_dict())
    session['username'] = request.form['username']
    return redirect(url_for('entry'))    
    
if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
          port=int(os.environ.get('PORT')),
          debug=True)