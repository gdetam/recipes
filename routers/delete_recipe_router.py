"""this file router for delete recipe."""

from app import app

from db.db_queries.get_recipe_query import get_recipe

from flask import flash, redirect, url_for

from models.db import db


@app.route('/recipes/<int:recipe_id>/delete', methods=['POST', 'GET'])
def delete_recipe(recipe_id: int):
    """Router for delete recipe."""
    recipe = get_recipe(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    flash(f'Рецепт успешно удалён!', 'success')
    return redirect(url_for('recipes'))
