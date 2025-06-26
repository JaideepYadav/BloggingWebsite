
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Email
class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=4, max=100)])
    body = TextAreaField("Body", validators=[DataRequired(), Length(min=10, max=500)])
    author = StringField("Author", validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField("Email", validators=[Email(message="Invalid email")])
