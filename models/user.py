"""this is users table structure."""

from time import time

from app import app, login_manager

from flask_login import UserMixin

import jwt

from models.db import db


@login_manager.user_loader
def load_user(user_id: int):
    """Query for Users table."""
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    """This is User class for table structure."""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    recipes = db.relationship('Recipes', backref='author', lazy=True)
    is_active = db.Column(db.Boolean, default=True)
    role = db.Column(db.Integer, default='2')

    def get_reset_token(self, expires_sec=1800):
        """Get reset token for change the password."""
        return jwt.encode({'reset_password': self.id, 'exp': time() + expires_sec},
                          app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        """Verify reset token for change the password."""
        try:
            id = jwt.decode(token,
                            app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return Users.query.get(id)

    def __rerp__(self):
        """Representation string of an Users object."""
        return f"Users('{self.username}', " \
               f"'{self.email}', " \
               f"'{self.image_file}'," \
               f"'{self.is_active}'," \
               f"'{self.role}')"
