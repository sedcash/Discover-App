from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField("First Name", validators=[DataRequired("Please enter your First Name")])
    last_name = StringField("Last Name", validators=[DataRequired("Please enter your Last Name")])
    email = StringField("Email", validators=[DataRequired("Please enter your Email"), Email("Please enter a valid email address")])
    password = PasswordField("Password", validators=[DataRequired("Please enter your Password"), Length(min=6, max=15, message="Your password must be at least 6 characters long and no longer than 15 characters")])
    submit = SubmitField("Sign Up")

class LoginForm(Form):
    email = StringField("Email", validators=[DataRequired("Please enter your Email"), Email("Please enter a valid email address")])
    password = PasswordField("Password", validators=[DataRequired("Please enter your Password")])
    submit = SubmitField("Sign In")

class AddressForm(Form):
    address = StringField("Address", validators=[DataRequired("Please type in a address")])
    submit = SubmitField("Search")