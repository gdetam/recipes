"""this is registration form for registration users."""

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField

from models.user import Users

from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


class RegistrationForm(FlaskForm):
    """Registration form for registration users."""

    username = StringField('Имя пользователя',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Электронная почта',
                        validators=[DataRequired(), Email()])
    picture = FileField('Выберите фото профиля',
                        validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    password = PasswordField('Пароль',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        """Validate username in registration form."""
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Это имя уже существует!')

    def validate_email(self, email):
        """Validate email in registration form."""
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Этот почтовый адрес уже существует!')
