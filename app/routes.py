from app import app
from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from app.forms import LoginForm,UserEditForm
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
		if form.email.data == app.config['ADMIN_EMAIL']:
			user = User.query.filter_by(email=form.email.data).first()
			if user is None or not user.check_password(form.password.data):
				return redirect(url_for('login'))
			login_user(user)
			return redirect(url_for('index'))
		else:
			# not admin
			return redirect(url_for('login'))

	return render_template('login.html', title='Antony Login', form=form)

@app.route('/logout/')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))


@app.route('/profile/Antony')
def profile():
	user = User.query.filter_by(email=app.config['ADMIN_EMAIL']).first()
	return render_template('profile.html', title='Profile (Antony)')



@app.route('/profile/edit', methods=['GET','POST'])
@login_required
def profile_edit():
	if current_user.email != app.config['ADMIN_EMAIL']:
		return redirect(url_for('index'))

	user = User.query.filter_by(email=app.config['ADMIN_EMAIL'])
	form = UserEditForm()
	if form.validate_on_submit():
		user.username = form.username.data
		user.firstname = form.firstname.data
		user.lastname = form.lastname.data
		user.email = form.email.data
		user.about_me = form.about_me.data
		user.title = form.title.data
		user.company = form.company.data

		db.session.commit()
		return redirect(url_for('profile'))

	elif request.method == 'GET':
		form.username.data = user.username
		form.firstname.data = user.firstname
		form.lastname.data = user.lastname
		form.email.data = user.email
		form.about_me.data = user.about_me
		form.title.data = user.title
		form.company.data = user.company

	return render_template('profile.html', title='Profile Edit (Antony)', form=form)
