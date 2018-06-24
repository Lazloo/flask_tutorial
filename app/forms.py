from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# For each field, an object is created as a class variable in the LoginForm class. Each field is given a description
# or label as a first argument.
class LoginForm(FlaskForm):
    # The DataRequired validator simply checks that the field is not submitted empty.
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')