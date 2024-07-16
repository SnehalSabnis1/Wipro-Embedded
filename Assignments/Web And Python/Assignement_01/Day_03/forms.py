from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ClaimForm(FlaskForm):
    policy_number = StringField('Policy Number', validators=[DataRequired()])
    claim_amount = FloatField('Claim Amount', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    claimant_name = StringField('Claimant Name', validators=[DataRequired()])
    claimant_email = StringField('Claimant Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit Claim')

