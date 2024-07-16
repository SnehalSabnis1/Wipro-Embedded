class Claim:
    def __init__(self, policy_number, claim_amount, description, claimant_name, claimant_email):
        self.policy_number = policy_number
        self.claim_amount = claim_amount
        self.description = description
        self.claimant_name = claimant_name
        self.claimant_email = claimant_email

    def save(self):
        # Pseudo code to save the claim to the database
        pass
