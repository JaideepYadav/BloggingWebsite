
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Email
class Signup(FlaskForm):
    user = StringField("User", validators=[DataRequired(), Length(min=4, max=100)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField("Email", validators=[Email(message="Invalid email")])
class Login(FlaskForm):
    email=StringField("Email", validators=[Email(message="Invalid email")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2, max=25)])


    
