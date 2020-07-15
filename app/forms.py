from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, TextAreaField,SubmitField
from wtforms.validators import DataRequired, Email, TextAreaField, Length


class LoginForm(FlaskForm):
    email = StringField('Email address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class UserEditForm(FlaskForm):
    username = StringField('Username', validators[DataRequired()])
    firstname = StringField('Firstname'])
    lastname = StringField('Lastname')
    email = StringField('Email', validators[DataRequired(),Email()])
    Password = StringField('Username', validators[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=500)])
    title =  StringField('Job title'])
    company =  StringField('Company or Freelancer')
