"""this file router for login page."""

from app import app, bcrypt

from flask import flash, redirect, render_template, request, url_for

from flask_login import current_user, login_user

from forms.login_form import LoginForm

from models.user import Users


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Router for login page."""
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Ошибка! Проверьте электронную почту или пароль.', 'danger')
    return render_template('login.html',
                           title='Вход',
                           form=form)
