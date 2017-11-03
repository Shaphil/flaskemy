from flask import render_template

from flaskemy import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return str(app.config)
