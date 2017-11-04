from flask import render_template, request, session

from flaskemy import app, db
from flaskemy.models import User, Task


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['user_name']
        email = request.form['user_email']
        password = request.form['user_password']
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['user_name']
        password = request.form['user_password']
        user = User.query.filter_by(name=name).first()
        if user and password == user.password:
            logged_in_user = {'name': user.name, 'id': user.id}
            session['user'] = logged_in_user
            tasks = Task.query.filter_by(user_id=user.id).all()
            return render_template('index.html', tasks=tasks)

        error = 'Invalid username/password'
        return render_template('login.html', error=error)

    return render_template('login.html')
