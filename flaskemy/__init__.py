from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flaskemy.config import *

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)


import flaskemy.views
