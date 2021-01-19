"""this file router for users page."""

from app import app

from db.db_queries.get_users_for_page_query import get_users_for_page

from flask import render_template

from routers.login_required import login_required


@app.route('/users')
@login_required(default_role=1)
def users():
    """Router for users page."""
    users = get_users_for_page()
    return render_template('users.html',
                           users=users)
