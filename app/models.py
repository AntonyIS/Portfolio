from app import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(124), index=True, unique=True)
	firstname = db.Column(db.String(124))
	lastname = db.Column(db.String(124))
	email = db.Column(db.String(124))
	password = db.Column(db.String(200))
	avatar = db.Column(db.String(124))
	about_me = db.Column(db.String(500))
	title = db.Column(db.String(124))
	company = db.Column(db.String(124))
	projects = db.relationship('Project', backref='developer', lazy='dynamic')


	def __repr__(self):
		return "<Developer: {} >".format(self.username)


class Project(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(124))
	body =  db.Column(db.String(500))
	avatar = db.Column(db.String(124))
	tech =  db.Column(db.String(124))
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	def __repr__(self):
		return "<Prpject: {} >".format(self.title)

