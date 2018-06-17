from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return '<h1>Main Hello World!</h1>'

@main.route('meals/')
def meals():
    meals = {
        "Learn Python The Hard Way": {
            "author": "Shaw, Zed",
            "rating": "3.92",
            "image": "ef0ceaab-32a8-47fb-ba13-c0b362d970da.jpg"
        }
    }
    # passing data to the template
    return render_template("meals.html", meals=meals)


@main.route('recipes/')
def recipes():
    meals = {}
    # passing data to the template
    return render_template("recipes.html", meals=meals)


@main.route('foods/')
def foods():
    meals = {}
    # passing data to the template
    return render_template("foods.html", meals=meals)


@main.route('exercise/')
def exercise():
    meals = {}
    # passing data to the template
    return render_template("exercise.html", meals=meals)
