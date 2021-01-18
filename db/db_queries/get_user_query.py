"""query for Users table for get user."""

from models.user import Users


def get_user(user_id: int):
    """Query for Users table."""
    user = Users.query \
                .get(user_id)
    return user
