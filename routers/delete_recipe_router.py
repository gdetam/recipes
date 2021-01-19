"""this file router for delete recipe."""

from app import app

from db.db_queries.get_recipe_query import get_recipe

from flask import abort, flash, redirect, url_for

from flask_login import current_user

from models.db import db
from models.user import Users

from routers.login_required import login_required


@app.route('/recipes/<int:recipe_id>/delete', methods=['POST', 'GET'])
@login_required(default_role=(1 if Users.role == 1 else 2))
def delete_recipe(recipe_id: int):
    """Router for delete recipe."""
    recipe = get_recipe(recipe_id)
    if recipe.author == current_user or current_user.role == 1:
        db.session.delete(recipe)
        db.session.commit()
        flash(f'Рецепт успешно удалён!', 'success')
        return redirect(url_for('recipes'))
    else:
        abort(403)
