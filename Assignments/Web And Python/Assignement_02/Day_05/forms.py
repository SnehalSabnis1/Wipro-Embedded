from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TimeField, SubmitField
from wtforms.validators import DataRequired

class RouteForm(FlaskForm):
    name = StringField('Route Name', validators=[DataRequired()])
    start_location = StringField('Start Location', validators=[DataRequired()])
    end_location = StringField('End Location', validators=[DataRequired()])
    submit = SubmitField('Add Route')

class ScheduleForm(FlaskForm):
    route_id = IntegerField('Route ID', validators=[DataRequired()])
    departure_time = TimeField('Departure Time', validators=[DataRequired()])
    arrival_time = TimeField('Arrival Time', validators=[DataRequired()])
    submit = SubmitField('Add Schedule')



