"""query for Categories table for get categories list."""

from models.category import Categories


def get_categories_list():
    """Query for Categories table."""
    categories_list = [(cat.id, cat.name) for cat in Categories.query.order_by(Categories.name).all()]
    return categories_list
