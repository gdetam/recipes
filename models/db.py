"""this file initializes connection for data base and SQLAlchemy."""

from app import app

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)
