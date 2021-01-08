"""this file router for selected category page."""

from app import app

from db.db_queries.get_category_detail_query import get_recipes_by_selected_category

from flask import render_template


@app.route('/categories/<int:category_id>', methods=['POST', 'GET'])
def category_detail(category_id: int):
    """Router for selected category page."""
    recipes = get_recipes_by_selected_category(category_id)
    return render_template('recipes.html',
                           recipes=recipes)
