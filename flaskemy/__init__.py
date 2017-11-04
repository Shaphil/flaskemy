import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

# Application configuration
DB_NAME = 'flaskemy.db'
DB_PATH = os.path.join(basedir, DB_NAME)

# SQLAlchemy configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)

import flaskemy.views.general
