from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TrafficQueryForm(FlaskForm):
    user_location = StringField('Your Location', validators=[DataRequired()])
    destination = StringField('Destination', validators=[DataRequired()])
    submit = SubmitField('Get Traffic Info')

