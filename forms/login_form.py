"""this is login form for users."""

from flask_wtf import FlaskForm

from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """Login form for users."""

    email = StringField('Электронная почта',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль',
                             validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
