"""this is recipe form for add recipe."""

from db.db_queries.get_categories_query import get_categories_list

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField

from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class RecipeForm(FlaskForm):
    """Recipe form for add recipe."""

    name = StringField('Название рецепта',
                       validators=[DataRequired(), Length(min=2, max=40)])
    ingredients = TextAreaField('Ингредиенты',
                                validators=[DataRequired(), Length(min=2, max=200)])
    description = TextAreaField('Описание',
                                validators=[DataRequired(), Length(min=2, max=500)])
    categories_list = get_categories_list()
    category = SelectField('Категория:',
                           coerce=int,
                           validators=[DataRequired()],
                           choices=categories_list)
    picture = FileField('Загрузить фото:',
                        validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Сохранить')
