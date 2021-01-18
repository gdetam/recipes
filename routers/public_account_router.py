"""this file router for public account page."""

from app import app

from db.db_queries.get_user_query import get_user

from flask import render_template, url_for

from forms.update_account_form import UpdateAccountForm


@app.route('/account/public/<int:user_id>', methods=['POST', 'GET'])
def public_account(user_id: int):
    """Router for public account page."""
    form = UpdateAccountForm()
    user = get_user(user_id)
    form.username.data = user.username
    recipes = user.recipes
    image_file = url_for('static',
                         filename='photos/' + user.image_file)
    return render_template('public_account.html',
                           title='Профиль',
                           image_file=image_file,
                           recipes=recipes,
                           form=form,
                           user=user)
