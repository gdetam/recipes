"""this file router for categories page."""

from app import app

from flask import render_template

from db.db_queries.get_categories_query import get_categories_list


@app.route('/categories')
def categories():
    """Router for categories page."""
    categories = get_categories_list()
    return render_template('categories.html',
                           categories=categories)
