"""query for Categories table for get user for delete and redirect recipe."""

from config import DELETE_USER_ID

from models.recipe import Recipes
from models.user import Users


def get_user_for_delete():
    """Query for Users table."""
    delete_user = Users.query \
                       .get(DELETE_USER_ID)
    return delete_user


def redirect_recipe(user_id: int):
    """Query for Recipes table."""
    recipes = Recipes.query \
                     .filter(user_id == Recipes.user_id) \
                     .all()
    return recipes
