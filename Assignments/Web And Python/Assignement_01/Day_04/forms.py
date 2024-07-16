from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class PolicyForm(FlaskForm):
    policy_number = StringField('Policy Number', validators=[DataRequired(), Length(min=1, max=20)])
    policy_holder_name = StringField('Policy Holder Name', validators=[DataRequired(), Length(min=1, max=100)])
    coverage_amount = DecimalField('Coverage Amount', validators=[DataRequired(), NumberRange(min=0)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Save Policy')

