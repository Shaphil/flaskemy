from flask import render_template, request

from flaskemy import app, db
from flaskemy.models import User


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
