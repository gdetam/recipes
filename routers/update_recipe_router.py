"""this file router for update recipe."""

from datetime import datetime

from app import app

from db.db_queries.get_recipe_query import get_recipe

from flask import flash, redirect, render_template, request, url_for

from forms.recipe_form import RecipeForm

from models.db import db


@app.route('/recipes/<int:recipe_id>/update', methods=['POST', 'GET'])
def update_recipe(recipe_id: int):
    """Router for update recipe."""
    recipe = get_recipe(recipe_id)
    form = RecipeForm()
    if form.validate_on_submit():
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
        form.category.data = recipe.category_id
    categories = RecipeForm.categories_list

    return render_template('create_recipe.html',
                           title='Редактирование рецепта',
                           form=form,
                           categories=categories,
                           legend='Редактирование рецепта')
