"""this is role_users table structure."""

from models.db import db


role_users = db.Table('role_users', db.metadata,
                      db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
                      db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
                      )
