from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, TextAreaField,SubmitField
from wtforms.validators import DataRequired, IsEqual


class Login(FlaskForm):
    email = StringField('Email address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
