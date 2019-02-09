import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId





app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipesdb'
app.config["MONGO_URI"] = 'mongodb://admin-1:family_recipes1@ds125125.mlab.com:25125/recipesdb'



mongo = PyMongo(app)



@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("index.html", 
        recipes=mongo.db.recipes.find())

@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    
    
    return render_template("recipe.html", recipe=the_recipe)

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', 
    serves=mongo.db.serves.find(), 
    cooking_duration=mongo.db.cooking_duration.find(), 
    cuisine_type=mongo.db.cuisine_type.find(),
    meal_type=mongo.db.meal_type.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)