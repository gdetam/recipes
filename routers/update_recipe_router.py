"""this file router for update recipe."""

from datetime import datetime

from app import app

from db.db_queries.get_recipe_query import get_recipe

from flask import abort, flash, redirect, render_template, request, url_for

from flask_login import current_user

from forms.recipe_form import RecipeForm

from models.db import db
from models.user import Users

from routers.login_required import login_required
from routers.picture_saver import save_picture


@app.route('/recipes/<int:recipe_id>/update', methods=['POST', 'GET'])
@login_required(default_role=(1 if Users.role == 1 else 2))
def update_recipe(recipe_id: int):
    """Router for update recipe."""
    recipe = get_recipe(recipe_id)

    if recipe.author == current_user or current_user.role == 1:
        form = RecipeForm()
        if form.validate_on_submit():
            picture_file = save_picture(form.picture.data)
            recipe.image_file = picture_file
            recipe.name = form.name.data
            recipe.ingredients = form.ingredients.data
            recipe.description = form.description.data
            recipe.category_id = form.category.data
            recipe.date_updated = datetime.utcnow()
            db.session.commit()
            flash(f'Изменения успешно сохранены!', 'success')
            return redirect(url_for('recipes'))
        elif request.method == 'GET':
            form.name.data = recipe.name
            form.ingredients.data = recipe.ingredients
            form.description.data = recipe.description
            form.picture.data = recipe.image_file
            form.category.data = recipe.category_id
        image_file = url_for('static',
                             filename='recipe_photos/' + recipe.image_file)
        categories = RecipeForm.categories_list

        return render_template('create_recipe.html',
                               title='Редактирование рецепта',
                               form=form,
                               categories=categories,
                               image_file=image_file,
                               legend='Редактирование рецепта')
    else:
        abort(403)
