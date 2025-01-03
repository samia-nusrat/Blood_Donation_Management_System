# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DonorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    blood_group = StringField('Blood Group', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    submit = SubmitField('Register')

class RequestForm(FlaskForm):
    blood_group = StringField('Blood Group', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    submit = SubmitField('Request Blood')

