import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId





app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipesdb'
app.config["MONGO_URI"] = 'mongodb://admin-1:family_recipes1@ds125125.mlab.com:25125/recipesdb'
app.secret_key = os.getenv("SECRET", "secret key")


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

@app.route('/insert_serving_size', methods=["POST"])
def insert_serving_size():
    serving_sizes = mongo.db.serves
    serving_sizes.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))

@app.route('/insert_cooking_duration', methods=["POST"])
def insert_cooking_duration():
    cooking_durations = mongo.db.cooking_duration
    cooking_durations.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))
    
@app.route('/insert_cuisine_type', methods=["POST"])
def insert_cuisine_type():
    cuisine_types = mongo.db.cuisine_type
    cuisine_types.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))
    
@app.route('/insert_meal_type', methods=["POST"])
def insert_meal_type():
    meal_types = mongo.db.meal_type
    
    """ need to add functionality to check if the type already exists"""
    added_meal_type = request.form["meal_type"]
    print(added_meal_type)
    
    meal_types.insert_one(request.form.to_dict())
    
    
    
    
    return redirect(url_for('add_recipe'))
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)