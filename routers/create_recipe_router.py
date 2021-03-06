"""this file router for create recipe page."""

from datetime import datetime

from app import app

from flask import flash, redirect, \
                  render_template, request, \
                  url_for

from flask_login import current_user

from forms.recipe_form import RecipeForm

from models.db import db
from models.recipe import Recipes
from models.user import Users

from routers.login_required import login_required
from routers.picture_saver import save_picture


@app.route('/recipe/create', methods=['POST', 'GET'])
@login_required(default_role=(1 if Users.role == 1 else 2))
def create_recipe():
    """Router for create recipe page."""
    form = RecipeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            picture_file = save_picture(form.picture.data)
            user_id = current_user.id
            recipe = Recipes(name=form.name.data,
                             ingredients=form.ingredients.data,
                             description=form.description.data,
                             image_file=picture_file,
                             date_posted=datetime.utcnow(),
                             date_updated=datetime.utcnow(),
                             category_id=form.category.data,
                             user_id=user_id)
            db.session.add(recipe)
            db.session.commit()
            flash(f'Рецепт {form.name.data} сохранен!', 'success')
            return redirect(url_for('recipes'))
    elif request.method == 'GET':
        categories = RecipeForm.categories_list

        return render_template('create_recipe.html',
                               title='Добавление рецепта',
                               form=form,
                               categories=categories,
                               legend='Добавление рецепта')
