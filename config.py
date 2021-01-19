"""this is config parser for settings.ini file."""

import configparser


# create a parser object
config = configparser.ConfigParser()
# read the config
config.read('E:/Python/recipes/settings.ini')
CONNECTION_FOR_ENGINE = config['CONNECTION_FOR_ENGINE']['CONNECTION_FOR_ENGINE']
TOP_SECRET_KEY = config['TOP_SECRET_KEY']['TOP_SECRET_KEY']
MAIL_SERVER = config['MAIL_SERVER']['MAIL_SERVER']
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = config['MAIL_USERNAME']['MAIL_USERNAME']
MAIL_PASSWORD = config['MAIL_PASSWORD']['MAIL_PASSWORD']
SQLALCHEMY_TRACK_MODIFICATIONS = False

LIMIT = 2
