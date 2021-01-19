"""this file initializes the flask project settings."""

from config import CONNECTION_FOR_ENGINE, MAIL_PASSWORD, \
                   MAIL_PORT, MAIL_SERVER, MAIL_USERNAME, \
                   MAIL_USE_SSL, MAIL_USE_TLS, TOP_SECRET_KEY, \
                   SQLALCHEMY_TRACK_MODIFICATIONS

from flask import Flask

from flask_bcrypt import Bcrypt

from flask_login import LoginManager

from flask_mail import Mail


app = Flask(__name__)

app.config['SECRET_KEY'] = TOP_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_FOR_ENGINE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

mail = Mail(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
