from app import app
from flask import render_template
from app.forms import LoginForm


user = {'name':'allan', 'points':36}

@app.route('/')
@app.route('/index')
def index():
    return render_template("welcome.html", title="Welcome", user=user)

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html', form=form, title = 'Sign In')