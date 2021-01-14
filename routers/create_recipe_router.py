"""this file router for create recipe page."""

from datetime import datetime

from app import app

from flask import flash, redirect, \
                  render_template, request, \
                  url_for

from forms.recipe_form import RecipeForm

from models.db import db
from models.recipe import Recipes


@app.route('/recipe/create', methods=['POST', 'GET'])
def create_recipe():
    """Router for create recipe page."""
    form = RecipeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            recipe = Recipes(name=form.name.data,
                             ingredients=form.ingredients.data,
                             description=form.description.data,
                             date_posted=datetime.utcnow(),
                             date_updated=datetime.utcnow(),
                             category_id=form.category.data)
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
