import os

# Get application path
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Application configuration
    DB_NAME = 'flaskemy.db'
    DB_PATH = os.path.join(basedir, DB_NAME)

    # SQLAlchemy configuration
    SQLALCHEMY_DATABASR_URI = 'sqlite:///' + DB_PATH
    SQLALCHEMY_track_modifications = False
