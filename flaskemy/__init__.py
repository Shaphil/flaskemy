from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flaskemy.settings.DevelopmentConfig')
db = SQLAlchemy(app)

import flaskemy.views.general
import flaskemy.views.auth
