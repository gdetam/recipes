"""this file router for account page."""

from app import app

from flask import flash, redirect, render_template, request, url_for

from flask_login import current_user

from forms.update_account_form import UpdateAccountForm

from models.db import db
from models.user import Users

from routers.login_required import login_required
from routers.picture_saver import save_picture


@app.route('/account', methods=['POST', 'GET'])
@login_required(default_role=(1 if Users.role == 1 else 2))
def account():
    """Router for account page."""
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Изменения успешно сохранены!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    recipes = current_user.recipes
    image_file = url_for('static',
                         filename='photos/' + current_user.image_file)
    return render_template('account.html',
                           title='Профиль',
                           image_file=image_file,
                           recipes=recipes,
                           legend='Редактирование профиля',
                           form=form)
