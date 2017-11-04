from flask import render_template, request

from flaskemy import app, db
from flaskemy.models import Task


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Add validity check for task name
        task = Task(name=request.form['task_name'])
        db.session.add(task)
        db.session.commit()

    # there should be a sanity check in case the db doesn't exist
    tasks = db.session.query(Task)
    return render_template('index.html', tasks=tasks)
