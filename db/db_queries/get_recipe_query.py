"""query for Recipes table for get recipe."""

from models.recipe import Recipes


def get_recipe(recipe_id: int):
    """Query for Recipes table."""
    recipe = Recipes.query \
                    .get(recipe_id)
    return recipe
