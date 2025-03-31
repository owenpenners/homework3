from app import myapp_obj
from flask import render_template
from flask import redirect
from app.forms import LoginForm, RecipeForm
from app.models import User, Recipe
from app import db
# from <X> import <Y>
"""
Displays a list of all recipes
"""
@myapp_obj.route("/")
def main():
    recipes = Recipe.query.all()
    return render_template("recipes.html", recipes=recipes)
"""
Displays a list of all recipes
"""
@myapp_obj.route("/recipes")
def recipes():
    recipes = Recipe.query.all() # retrieve recipes
    return render_template("recipes.html", recipes=recipes)

@myapp_obj.route("/accounts")
def users():
    return "My USER ACCOUNTS"
"""
Allows user to add a new recipe to the list given that the user entries validate the form
Adds new recipe to data base
"""
@myapp_obj.route("/recipe/new", methods=['GET', 'POST'])
def new():
    form = RecipeForm()
    if form.validate_on_submit():
        r = Recipe(title=form.title.data, description=form.description.data, ingredients=form.ingredients.data, instructions=form.instructions.data) # initializes new recipe object
        db.session.add(r) # adds to databse
        db.session.commit() # commits new database
        print(f"title = {form.title.data} description = {form.description.data} ingredients = {form.ingredients.data} instruction = {form.instructions.data}")
        return redirect("/")
    else:
        print("no submit")
    return render_template("newRecipe.html", form=form)

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f"Here is the input from the user {form.username.data} and {form.password.data}")
        return redirect("/")
    else:
        print("MOOOO MOOO")
    return render_template("login.html", form=form)
    # What is render template returning?
    #return str(type(render_template("login.html", form=form)))

"""
Displays the recipe at the index given+1 to account for user counting from 1
Checks for the boundries of the current recipes
"""
@myapp_obj.route("/recipe/<int:index>")
def showRecipe(index):
    all_recipes = Recipe.query.all() # retrieve recipes
    if index < 1 or index > len(all_recipes):
        return "Out of Bounds Error"
    requestRecipe = all_recipes[index-1] # lists begin at 0
    return render_template("printRecipe.html", recipe=requestRecipe)

"""
deleteRecipe(index) deletes the recipe at the index given + 1 to account for user counting from 1 first
"""
@myapp_obj.route("/recipe/<int:index>/delete")
def deleteRecipe(index):
    all_recipes = Recipe.query.all()
    if index < 1 or index > len(all_recipes):
        return "Out of Bounds Error"
    db.session.delete(all_recipes[index-1])
    db.session.commit()
    print(f"Index {index-1} deleted")
    return redirect("/")
