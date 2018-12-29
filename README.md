Credits:
https://www.incredibleegg.org/recipe/basic-scrambled-eggs/

Pretty Printed (Youtube Channel/author of video)
Credit for instructonal video using login example which I followed for my own implementation of authentication of a login system (very helpful video for using Mongodb and flask to check this kind of data):
https://www.youtube.com/watch?v=vVx1737auSE

Michael Parks (tutor) - 
Credit for image display on categories page  and ginja clean up of static file to easily access my assets.
Credit full graph functionality.

Niel McEwan(tutor) -
Credit for basic graph functionality in app.py

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('view_recipe.html', recipe=the_recipe, categories=all_categories)
    
@app.route('/view_count/<recipe_id>')
def view_count(recipe_id):
    mongo.db.recipes
    recipes.update({'_id': str(recipe_id)}, {'$inc': {'views': int(1)}})
    return url_for('view_recipe.html')    