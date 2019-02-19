import os
import unicodedata
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId








app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipesdb'
app.config["MONGO_URI"] = 'mongodb://admin-1:family_recipes1@ds125125.mlab.com:25125/recipesdb'
app.secret_key = os.getenv("SECRET", "secret key")


mongo = PyMongo(app)




    

@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template("index.html")



@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    
    return render_template("recipe.html", recipe=the_recipe)



@app.route('/add_recipe')
def add_recipe():
    """ Shows the addrecipe.html template, and supplies it with the current values stored within each collection"""
    """ Currently only the cuisine type and meal type collections returned sorted results"""
    return render_template('addrecipe.html', 
    serves = mongo.db.serves.find(), 
    cooking_duration=mongo.db.cooking_duration.find(), 
    cuisine_type=mongo.db.cuisine_type.find().sort("cuisine_type", 1),
    meal_type=mongo.db.meal_type.find().sort("meal_type", 1))




@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    
    recipes =  mongo.db.recipes
    authors = mongo.db.authors
    
    current_authors = []
    
    for author in authors.find().distinct('author'):
        current_authors.append(author)
    
    current_authors_string = ', '.join(current_authors).lower()
    
    new_author = request.form.get('author').lower()
    
    if request.method == 'POST':
        
        recipes.insert_one(request.form.to_dict())
        
        if new_author not in current_authors_string:
            authors.insert([{ "author": request.form['author']}])
       
    return redirect(url_for('search_recipes'))



@app.route('/insert_serves', methods=["POST"])
def insert_serves():
    serves_size = mongo.db.serves
    
    current_serves_size_list = []
        
    for type in serves_size.find().distinct('serves'):
        current_serves_size_list.append(type)
            
    current_serves_size_string = ', '.join(current_serves_size_list)
        
    new_serves_size = request.form.get('serves')
    
    if request.method == 'POST':
        if new_serves_size not in current_serves_size_list:
            serves_size.insert_one(request.form.to_dict())
        else:
            flash("We already have a serving size for '{}' people".format(new_serves_size))
    
    return redirect(url_for('add_recipe'))



@app.route('/insert_cooking_duration', methods=["POST"])
def insert_cooking_duration():
    cooking_duration = mongo.db.cooking_duration
    
    current_cooking_duration_list = []
        
    for type in cooking_duration.find().distinct('cooking_duration'):
        current_cooking_duration_list.append(type)
            
    current_cooking_duration_string = ', '.join(current_cooking_duration_list)
        
    
    new_cooking_duration = request.form.get('cooking_duration')
    
    
    if request.method == 'POST':
        if new_cooking_duration not in current_cooking_duration_string:
            cooking_duration.insert_one(request.form.to_dict())
        else:
            flash("We already have a cooking duration of '{}' minutes".format(new_cooking_duration))
    
    return redirect(url_for('add_recipe'))
    




@app.route('/insert_cuisine_type', methods=["POST"])
def insert_cuisine_type():
    cuisine_types = mongo.db.cuisine_type
    
    current_cuisine_types_list = []
        
    for type in cuisine_types.find().distinct('cuisine_type'):
        current_cuisine_types_list.append(type)
            
    current_cuisine_types_string = ', '.join(current_cuisine_types_list)
        
    
    new_cuisine_type = request.form.get('cuisine_type').lower()
    
    
    if request.method == 'POST':
        if new_cuisine_type not in current_cuisine_types_string:
            cuisine_types.insert_one(request.form.to_dict())
        else:
            flash("We already have a cuisine type called '{}'".format(new_cuisine_type))
    
    return redirect(url_for('add_recipe'))
    




@app.route('/insert_meal_type', methods=["POST"])
def insert_meal_type():
   
    meal_types = mongo.db.meal_type
    
    current_meal_types_list = []
        
    for type in meal_types.find().distinct('meal_type'):
        current_meal_types_list.append(type)
            
    current_meal_types_string = ', '.join(current_meal_types_list)
        
    
    new_meal_type = request.form.get('meal_type').lower()
    
    
    if request.method == 'POST':
        if new_meal_type not in current_meal_types_string:
            meal_types.insert_one(request.form.to_dict())
        else:
            flash("We already have a meal type called '{}'".format(new_meal_type))
    
    return redirect(url_for('add_recipe'))


@app.route('/delete_recipe/<recipe_id>', methods=['POST', 'GET'])
def delete_recipe(recipe_id):

    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    
    return redirect(url_for('search_recipes'))    

@app.route('/search_recipes', methods=['POST', 'GET'])
def search_recipes():
    
    search_field = request.form.get('search_field')
    search_value = request.form.get('search_values')
    print(search_value)
    
    if request.method == "POST" and search_value == None:
        print(search_value)
        
        
        return render_template('searchrecipes.html',
            recipes=mongo.db.recipes.find().sort(search_field, 1),
            authors=mongo.db.authors.find(),
            serves=mongo.db.serves.find(),
            cooking_duration=mongo.db.cooking_duration.find(),
            meal_type=mongo.db.meal_type.find(),
            cuisine_type=mongo.db.cuisine_type.find()
            )
        
    
    elif request.method == "POST" and search_value != "":
        
        
        
        return render_template('searchrecipes.html',
            recipes=mongo.db.recipes.find({search_field: search_value}),
            authors=mongo.db.authors.find(),
            serves=mongo.db.serves.find(),
            cooking_duration=mongo.db.cooking_duration.find(),
            meal_type=mongo.db.meal_type.find(),
            cuisine_type=mongo.db.cuisine_type.find()
            )
            
    return render_template('searchrecipes.html',
                recipes=mongo.db.recipes.find(),
                authors=mongo.db.author.find(),
                serves=mongo.db.serves.find(),
                cooking_duration=mongo.db.cooking_duration.find(),
                meal_type=mongo.db.meal_type.find(),
                cuisine_type=mongo.db.cuisine_type.find()
                )

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):

    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    
    
    return render_template('editrecipe.html', 
        recipe = the_recipe, 
        recipe_description=mongo.db.recipe_description.find(),
        recipe_instructions=mongo.db.recipe_instructions.find(),
        serves=mongo.db.serves.find(),
        cooking_duration=mongo.db.cooking_duration.find(),
        meal_type=mongo.db.meal_type.find(),
        cuisine_type=mongo.db.cuisine_type.find(),
        authors=mongo.db.author.find()
        )   


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'serves':request.form.get('serves'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_instructions': request.form.get('recipe_instructions'),
        'cooking_duration': request.form.get('cooking_duration'),
        'cuisine_type':request.form.get('cuisine_type'),
        'ingredients':request.form.get('ingredients'),
        'meal_type':request.form.get('meal_type'),
        'author':request.form.get('author'),
        
    })
    return redirect(url_for('search_recipes')) 



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)