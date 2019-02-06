import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipesdb'
app.config["MONGO_URI"] = 'mongodb://admin-1:family_recipes1@ds125125.mlab.com:25125/recipesdb'

mongo = PyMongo(app)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)