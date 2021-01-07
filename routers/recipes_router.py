"""this file router for recipes page."""

from app import app

from db.db_queries.get_recipe_for_page_query import get_recipes_for_page

from flask import render_template


@app.route('/recipes')
def recipes():
    """Router for recipes page."""
    recipes = get_recipes_for_page()
    return render_template('recipes.html',
                           recipes=recipes)
