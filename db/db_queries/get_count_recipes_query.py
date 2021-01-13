"""query for Recipes table for get count recipes."""

from models.recipe import Recipes


def get_count_recipes():
    """Query for Recipes table."""
    result: int = Recipes.query \
                         .count()
    return result
