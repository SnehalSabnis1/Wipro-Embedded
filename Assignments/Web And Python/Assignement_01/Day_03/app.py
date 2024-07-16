from flask import Flask, render_template, request, redirect, url_for, flash
from models import Claim
from forms import ClaimForm

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Route for displaying the claim form
@app.route('/', methods=['GET', 'POST'])
def submit_claim():
    form = ClaimForm()
    if form.validate_on_submit():
        new_claim = Claim(
            policy_number=form.policy_number.data,
            claim_amount=form.claim_amount.data,
            description=form.description.data,
            claimant_name=form.claimant_name.data,
            claimant_email=form.claimant_email.data
        )
        # Save the claim to the database (pseudo code)
        new_claim.save()
        flash('Claim submitted successfully!', 'success')
        return redirect(url_for('claim_confirmation'))
    return render_template('claim_form.html', form=form)

# Route for displaying the claim confirmation page
@app.route('/claim-confirmation')
def claim_confirmation():
    return render_template('claim_confirmation.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Start the application on port 5001 with debug mode enabled

