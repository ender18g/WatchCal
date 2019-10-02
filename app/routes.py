from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm



user = {'name':'allan', 'points':36}

@app.route('/')
@app.route('/index')
def index():
    return render_template("welcome.html", title="Welcome", user=user)

@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash(f"login requested for {form.email.data}")
        return redirect(url_for('index'))
    return render_template('login.html', form=form, title = 'Sign In')