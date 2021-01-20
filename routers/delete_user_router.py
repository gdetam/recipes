"""this file router for delete user."""

from app import app

from db.db_queries.get_user_for_delete_query import get_user_for_delete, \
                                                    redirect_recipe
from db.db_queries.get_user_query import get_user

from flask import flash, redirect, url_for

from models.db import db

from routers.login_required import login_required


@app.route('/users/<int:user_id>/delete', methods=['POST', 'GET'])
@login_required(default_role=1)
def delete_user(user_id: int):
    """Router for delete user."""
    user = get_user(user_id)
    del_user = get_user_for_delete()
    recipes = redirect_recipe(user_id)
    for recipe in recipes:
        recipe.author = del_user
    db.session.delete(user)
    db.session.commit()
    flash(f'Профиль успешно удалён!', 'success')
    return redirect(url_for('users'))
