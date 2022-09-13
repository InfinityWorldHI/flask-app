from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class NewUserForm(FlaskForm):
	username = StringField("Username", 
		validators=[
		DataRequired(),
		Length(min=2, max=30)])

	number = StringField("Number", 
		validators=[
		DataRequired(),
		Length(min=7, max=8)])

	submit = SubmitField("Add")


class EditUserForm(FlaskForm):
	username_up = StringField("Username", 
		validators=[
		DataRequired(),
		Length(min=2, max=30)],
		render_kw={'readonly': True})

	number_up = StringField("Number", 
		validators=[
		DataRequired(),
		Length(min=7, max=8)])

	submit = SubmitField("Edit")
