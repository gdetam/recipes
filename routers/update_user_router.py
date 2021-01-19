"""this file router for update users."""

from app import app

from db.db_queries.get_user_query import get_user

from flask import flash, redirect, render_template, request, url_for

from forms.update_account_form import UpdateAccountForm

from models.db import db

from routers.login_required import login_required
from routers.picture_saver import save_picture


@app.route('/users/<int:user_id>/update', methods=['POST', 'GET'])
@login_required(default_role=1)
def update_user(user_id: int):
    """Router for update users."""
    user = get_user(user_id)
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            user.image_file = picture_file
        user.username = form.username.data
        user.email = form.email.data
        db.session.commit()
        flash(f'Изменения успешно сохранены!', 'success')
        return redirect(url_for('users'))
    elif request.method == 'GET':
        form.username.data = user.username
        form.email.data = user.email
    image_file = url_for('static',
                         filename='photos/' + user.image_file)
    return render_template('account.html',
                           title='Профиль',
                           image_file=image_file,
                           legend='Изменение профиля',
                           form=form,
                           user=user)
