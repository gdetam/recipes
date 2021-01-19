"""this is reset password form for user."""

from flask_wtf import FlaskForm

from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class ResetPasswordForm(FlaskForm):
    """Reset password form for user."""

    password = PasswordField('Пароль',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Сохранить')
