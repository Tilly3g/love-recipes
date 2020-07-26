import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'love_recipes'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


# 404 error page when incorrect URL used
@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404

# Page route for home page
@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template("index.html")


# Page route for recipe search page, found by clicking 'Search Recipes'
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html")


# Display results from using the search function
@app.route('/search_results', methods=['POST'])
def search_results():
    search = request.form.get('search')
    result = mongo.db.recipes.find_one({'recipe_name': {'$regex': '^' + search + '$', '$options': 'i'}})
    return render_template('results.html', recipe=result)


# This page is found by clicking 'Breakfast Recipes' on the recipe search page and shows all recipes with meal type 'Breakfast'
@app.route('/get_breakfast')
def get_breakfast():
    all_recipes = mongo.db.recipes.find()
    all_meals = mongo.db.meals.find()
    return render_template("breakfast.html", recipes=all_recipes, meals=all_meals)


# This page is found by clicking 'Lunch Recipes' on the recipe search page and shows all recipes with meal type 'Lunch'
@app.route('/get_lunch')
def get_lunch():
    all_recipes = mongo.db.recipes.find()
    all_meals = mongo.db.meals.find()
    return render_template("lunch.html", recipes=all_recipes, meals=all_meals)


# This page is found by clicking 'Snack Recipes' on the recipe search page and shows all recipes with meal type 'Snack'
@app.route('/get_snacks')
def get_snacks():
    all_recipes = mongo.db.recipes.find()
    all_meals = mongo.db.meals.find()
    return render_template("snacks.html", recipes=all_recipes, meals=all_meals)


# This page is found by clicking 'Dinner Recipes' on the recipe search page and shows all recipes with meal type 'Dinner'
@app.route('/get_dinner')
def get_dinner():
    all_recipes = mongo.db.recipes.find()
    all_meals = mongo.db.meals.find()
    return render_template("dinner.html", recipes=all_recipes, meals=all_meals)


# This page is found by clicking 'Dessert Recipes' on the recipe search page and shows all recipes with meal type 'Desserts'
@app.route('/get_desserts')
def get_desserts():
    all_recipes = mongo.db.recipes.find()
    all_meals = mongo.db.meals.find()
    return render_template("desserts.html", recipes=all_recipes, meals=all_meals)


# Page to view each recipe singularly and in full
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipeView.html', recipe=the_recipe)


# Page for adding a new recipe
@app.route('/add_recipe')
def add_recipe():
    all_meals = mongo.db.meals.find()
    return render_template('addrecipe.html', meals=all_meals)


# File path for adding new recipe to the database, takes you to view the new recipe once added
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipe_id = recipes.insert_one(request.form.to_dict()).inserted_id
    return redirect(url_for('view_recipe', recipe_id=recipe_id))


# Page for editing a recipe - prefilled with recipe info and can then be updated
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_meals = mongo.db.meals.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           meals=all_meals)


#Add updates to database and view newly edited recipe
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'prep_timehrs': request.form.get('prep_timehrs'),
        'prep_timemins': request.form.get('prep_timemins'),
        'description': request.form.get('description'),
        'meal_type': request.form.get('meal_type'),
        'ingredients': request.form.get('ingredients'),
        'required_tools': request.form.get('required_tools'),
        'preparation_steps': request.form.get('preparation_steps'),
    })
    return redirect(url_for('view_recipe', recipe_id=recipe_id))


# File path for deleting recipes, takes you to a page confirming deletion
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return render_template('deleted.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
