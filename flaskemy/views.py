from flask import render_template

from flaskemy import app, db
from flaskemy.models import Task


@app.route('/')
def index():
    # there should be a sanity check in case the db doesn't exist
    tasks = db.session.query(Task)
    return render_template('index.html', tasks=tasks)
