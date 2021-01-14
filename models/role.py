"""this is role table structure."""

from models.db import db
from models.role_users import role_users


class Role(db.Model):
    """This is Role class for table structure."""

    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.String)
    user = db.relationship('Users', secondary=role_users)
