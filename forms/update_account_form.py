"""this is update account form for user."""

from flask_login import current_user

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField

from models.user import Users

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError


class UpdateAccountForm(FlaskForm):
    """Update account form for user."""

    username = StringField('Имя пользователя',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Электронная почта',
                        validators=[DataRequired(), Email()])
    picture = FileField('Изменить фото профиля',
                        validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Сохранить')

    def validate_username(self, username):
        """Validate username in update account form."""
        if username.data != current_user.username:
            user = Users.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Это имя уже существует!')

    def validate_email(self, email):
        """Validate email in update account form."""
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Эта электронная почта уже существует!')
