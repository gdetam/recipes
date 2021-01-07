"""this file router for recipe detail page."""

from app import app

from db.db_queries.get_recipe_query import get_recipe

from flask import render_template


@app.route('/recipes/<int:recipe_id>')
def recipe_detail(recipe_id: int):
    """Router for recipe detail page."""
    recipe = get_recipe(recipe_id)
    return render_template('recipe_detail.html',
                           recipe=recipe)
