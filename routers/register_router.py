"""this file router for register page."""

from app import app, bcrypt

from flask import flash, redirect, render_template, url_for

from flask_login import current_user

from forms.registration_form import RegistrationForm

from models.db import db
from models.user import Users

from routers.picture_saver import save_picture


@app.route('/register', methods=['POST', 'GET'])
def register():
    """Router for register page."""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        picture_file = save_picture(form.picture.data)
        current_user.image_file = picture_file
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data,
                     email=form.email.data,
                     image_file=picture_file,
                     password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Аккаунт {form.username.data} успешно зарегистрирован! Войдите в систему.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html',
                           title='Регистрация',
                           form=form)
