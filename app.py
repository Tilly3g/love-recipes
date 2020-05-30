import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'love_recipes'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


# Page route for home page

@app.route('/home_page')
def home_page():
    return render_template("index.html", recipes=mongo.db.recipes.find())

# Page route for recipe search page
# Currently set as main path for testing
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html")


@app.route('/get_breakfast')
def get_breakfast():
    all_recipes = mongo.db.recipes.find()
    all_meals = mongo.db.meals.find()
    return render_template("breakfast.html", recipes=all_recipes, meals=all_meals)


@app.route('/get_lunch')
def get_lunch():
    all_recipes = mongo.db.recipes.find()
    all_meals = mongo.db.meals.find()
    return render_template("lunch.html", recipes=all_recipes, meals=all_meals)


@app.route('/get_snacks')
def get_snacks():
    all_recipes = mongo.db.recipes.find()
    all_meals = mongo.db.meals.find()
    return render_template("snacks.html", recipes=all_recipes, meals=all_meals)


@app.route('/get_dinner')
def get_dinner():
    all_recipes = mongo.db.recipes.find()
    all_meals = mongo.db.meals.find()
    return render_template("dinner.html", recipes=all_recipes, meals=all_meals)


@app.route('/get_desserts')
def get_desserts():
    all_recipes = mongo.db.recipes.find()
    all_meals = mongo.db.meals.find()
    return render_template("desserts.html", recipes=all_recipes, meals=all_meals)


#File paths for adding a new recipe
@app.route('/add_recipe')
def add_recipe():
    all_meals = mongo.db.meals.find()
    all_tools = mongo.db.tools.find()
    return render_template('addrecipe.html',
                           meals=all_meals, tools=all_tools)

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
