"""this is config parser for settings.ini file."""

import configparser


# create a parser object
config = configparser.ConfigParser()
# read the config
config.read('E:/Python/recipes/settings.ini')
CONNECTION_FOR_ENGINE = config['CONNECTION_FOR_ENGINE']['CONNECTION_FOR_ENGINE']
TOP_SECRET_KEY = config['TOP_SECRET_KEY']['TOP_SECRET_KEY']
SQLALCHEMY_TRACK_MODIFICATIONS = False
