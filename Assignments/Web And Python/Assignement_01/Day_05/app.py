
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
import os

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

class Claim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_number = db.Column(db.String(100), nullable=False)
    claim_amount = db.Column(db.Float, nullable=False)
    claim_description = db.Column(db.Text, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def submit_claim():
    if request.method == 'POST':
        policy_number = request.form['policy_number']
        claim_amount = request.form['claim_amount']
        claim_description = request.form['claim_description']
        
        # Server-side validation
        if not policy_number or not claim_amount or not claim_description:
            flash('All fields are required!')
            return redirect(url_for('submit_claim'))

        # Create a new claim record
        new_claim = Claim(policy_number=policy_number, claim_amount=claim_amount, claim_description=claim_description)
        
        try:
            db.session.add(new_claim)
            db.session.commit()
            flash('Claim submitted successfully!')
            return redirect(url_for('submit_claim'))
        except Exception as e:
            flash(f'Error submitting claim: {e}')
            return redirect(url_for('submit_claim'))

    return render_template('claim_form.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5001, debug=True)  # Start the application on port 5001 with debug mode enabled

