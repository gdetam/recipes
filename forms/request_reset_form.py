"""this is request reset form for send email to change the password."""

from flask_wtf import FlaskForm

from models.user import Users

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError


class RequestResetForm(FlaskForm):
    """Request reset form for send email to change the password."""

    email = StringField('Электронная почта',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Отправить')

    def validate_email(self, email):
        """Validate email in request reset form."""
        user = Users.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Эта электронная почта не зарегестрированна!')
