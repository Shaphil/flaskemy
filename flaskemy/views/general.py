from flask import render_template, request, session

from flaskemy import app, db
from flaskemy.models import Task


@app.route('/', methods=['GET', 'POST'])
def index():
    # there should be a sanity check in case the db doesn't exist
    if session.get('user'):
        user = session.get('user')
        if request.method == 'POST':
            # Add validity check for task name
            task = Task(name=request.form['task_name'], user_id=user['id'])
            db.session.add(task)
            db.session.commit()

        tasks = Task.query.filter_by(user_id=user['id']).all()
        return render_template('index.html', tasks=tasks)

    return render_template('index.html')
