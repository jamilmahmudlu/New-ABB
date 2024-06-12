from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    first_name = StringField(label = 'First Name', validators = [DataRequired(), Length(min=2, max=20)])
    last_name = StringField(label = 'Last Name', validators = [DataRequired(), Length(min=2, max=20)])
    phone = IntegerField(label = 'Phone Number', validators = [DataRequired()])
    fin_code = IntegerField(label = 'Fin Number', validators =[DataRequired()])