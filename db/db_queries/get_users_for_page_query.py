"""query for Users table for get users for page."""

from models.user import Users


def get_users_for_page():
    """Query for Users table."""
    users = Users.query \
                 .all()
    return users
