"""query for Recipes table for get recipes by selected category."""

from models.recipe import Recipes


def get_recipes_by_selected_category(category_id: int):
    """Query for Recipes table."""
    recipes = Recipes.query \
                     .filter(category_id == Recipes.category_id) \
                     .all()
    return recipes
