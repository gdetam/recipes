"""this is categories table structure."""

from models.db import db


class Categories(db.Model):
    """This is Categories class for table structure."""

    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
