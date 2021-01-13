"""this file router for random recipe page."""

import random

from app import app

from db.db_queries.get_count_recipes_query import get_count_recipes
from db.db_queries.get_recipe_query import get_recipe

from flask import render_template


@app.route('/recipe/random', methods=['GET'])
def random_recipe():
    """Router for random recipe page."""
    result: int = get_count_recipes()
    count_recipes = int(result)
    if count_recipes > 0:
        recipe_id = random.randint(1, count_recipes)
        recipe = get_recipe(recipe_id)
        return render_template('recipe_detail.html',
                               recipe=recipe)
    else:
        recipe = 0
        return render_template('recipe_detail.html',
                               recipe=recipe)
