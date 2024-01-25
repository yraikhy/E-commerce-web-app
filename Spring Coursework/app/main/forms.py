from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import Length, DataRequired

class SubmitForm(FlaskForm):
    submit = SubmitField()

class payForm(FlaskForm):
    full_name = StringField("What is your full name?", validators=[DataRequired(), Length(1, 20)])
    card_num = StringField("Enter your card number", validators=[DataRequired(), Length(1, 16)])
    cvc_num = StringField("Enter your CVC", validators=[DataRequired(), Length(1, 3)])
    pay = SubmitField()

