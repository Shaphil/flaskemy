import os


class Config(object):
    DEBUG = False
    SECRET_KEY = 'drogon'


basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(Config):
    # Application configuration
    DB_NAME = 'flaskemy.db'
    DB_PATH = os.path.join(basedir, DB_NAME)

    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False
