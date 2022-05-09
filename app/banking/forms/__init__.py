from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *

class upload_csv_file(FlaskForm):
    file=FileField()
    submit=SubmitField()
