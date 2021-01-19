"""this file login_required function, this function is supplemented roles."""

from functools import wraps

from flask import current_app

from flask_login import current_user


def login_required(default_role=2):
    """Define roles for access of page."""
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return current_app.login_manager.unauthorized()
            elif current_user.role != default_role and default_role != 2:
                return current_app.login_manager.unauthorized()
            return fn(*args, **kwargs)

        return decorated_view

    return wrapper
