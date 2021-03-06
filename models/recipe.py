"""this is recipes table structure."""

from datetime import datetime

from models.db import db


class Recipes(db.Model):
    """This is Recipes class for table structure."""

    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Categories', foreign_keys=[category_id])
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('Users', foreign_keys=[user_id])

    def __rerp__(self):
        """Representation string of an Recipes object."""
        return f"Recipes('{self.name}', " \
               f"'{self.category_id}', " \
               f"'{self.user_id}', " \
               f"'{self.date_posted}', " \
               f"'{self.date_updated}', " \
               f"'{self.image_file}')"
