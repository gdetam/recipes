"""this file initializes the flask project settings."""

from config import CONNECTION_FOR_ENGINE, TOP_SECRET_KEY, \
                   SQLALCHEMY_TRACK_MODIFICATIONS

from flask import Flask

from flask_bcrypt import Bcrypt

from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = TOP_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_FOR_ENGINE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
