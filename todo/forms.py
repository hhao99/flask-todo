from flask_wtf import FlaskForm
from wtforms import StringField,  BooleanField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    isDone = BooleanField('isDone')
    submit = SubmitField('Save')