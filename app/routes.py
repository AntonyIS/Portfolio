from app import app
from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from app.forms import LoginForm
from app.models import User

# home route
@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html', title='Home page')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect (url_for('index'))

	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None or not user.check_password(form.password.data):
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index'))
	return render_template('login.html', title='Antony Login', form=form)
