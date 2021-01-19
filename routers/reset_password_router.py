"""this file router for home page."""

from app import app, bcrypt, mail

from flask import flash, redirect, render_template, url_for

from flask_login import current_user

from flask_mail import Message

from forms.request_reset_form import RequestResetForm
from forms.reset_password_form import ResetPasswordForm

from models.db import db
from models.user import Users


def send_reset_email(user):
    """Send reset email for change password."""
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='sendmailflask@yandex.ru',
                  recipients=[user.email])
    msg.body = (f"""Для сброса пароля перейдите по ссылке:
    {url_for('reset_token', token=token, _external=True)}
    Если вы не отправляли сообщение, проигнорируйте данное письмо!
    """)
    mail.send(msg)


@app.route('/reset_password', methods=['POST', 'GET'])
def reset_request():
    """Router for reset password page."""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        # send reset email for change password
        send_reset_email(user)
        flash(f'На вашу электронную почту отправлено письмо!', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html',
                           title='Изменение пароля',
                           form=form)


@app.route('/reset_password/<token>', methods=['POST', 'GET'])
def reset_token(token):
    """Router for reset password page."""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = Users.verify_reset_token(token)
    if user is None:
        flash(f'Это недействительный или просроченный код!', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    # change password
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Ваш пароль успешно изменен! Войдите в систему.', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html',
                           title='Изменение пароля',
                           form=form)
