"""query for Recipes table for get recipes for page."""

from models.recipe import Recipes


def get_recipes_for_page():
    """Query for Recipes table."""
    recipes = Recipes.query \
                     .order_by(Recipes.date_posted.desc()) \
                     .all()
    return recipes
