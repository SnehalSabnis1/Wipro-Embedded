from flask import Blueprint, request, jsonify
from models import db, Policy, Claim

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return "Welcome to the Insurance Claim Processing System"

# CRUD operations for policies
@main_blueprint.route('/policy', methods=['POST'])
def create_policy():
    data = request.get_json()
    new_policy = Policy(
        policy_number=data['policy_number'],
        policy_holder_name=data['policy_holder_name'],
        policy_start_date=data['policy_start_date'],
        policy_end_date=data['policy_end_date'],
        premium_amount=data['premium_amount']
    )
    db.session.add(new_policy)
    db.session.commit()
    return jsonify({'message': 'New policy created'}), 201

@main_blueprint.route('/policy/<int:id>', methods=['GET'])
def get_policy(id):
    policy = Policy.query.get_or_404(id)
    return jsonify({
        'policy_number': policy.policy_number,
        'policy_holder_name': policy.policy_holder_name,
        'policy_start_date': policy.policy_start_date,
        'policy_end_date': policy.policy_end_date,
        'premium_amount': policy.premium_amount
    })

@main_blueprint.route('/policy/<int:id>', methods=['PUT'])
def update_policy(id):
    data = request.get_json()
    policy = Policy.query.get_or_404(id)
    policy.policy_number = data['policy_number']
    policy.policy_holder_name = data['policy_holder_name']
    policy.policy_start_date = data['policy_start_date']
    policy.policy_end_date = data['policy_end_date']
    policy.premium_amount = data['premium_amount']
    db.session.commit()
    return jsonify({'message': 'Policy updated'})

@main_blueprint.route('/policy/<int:id>', methods=['DELETE'])
def delete_policy(id):
    policy = Policy.query.get_or_404(id)
    db.session.delete(policy)
    db.session.commit()
    return jsonify({'message': 'Policy deleted'})

# CRUD operations for claims
@main_blueprint.route('/claim', methods=['POST'])
def create_claim():
    data = request.get_json()
    new_claim = Claim(
        claim_number=data['claim_number'],
        claim_date=data['claim_date'],
        claim_amount=data['claim_amount'],
        claim_status=data['claim_status'],
        policy_id=data['policy_id']
    )
    db.session.add(new_claim)
    db.session.commit()
    return jsonify({'message': 'New claim created'}), 201

@main_blueprint.route('/claim/<int:id>', methods=['GET'])
def get_claim(id):
    claim = Claim.query.get_or_404(id)
    return jsonify({
        'claim_number': claim.claim_number,
        'claim_date': claim.claim_date,
        'claim_amount': claim.claim_amount,
        'claim_status': claim.claim_status,
        'policy_id': claim.policy_id
    })

@main_blueprint.route('/claim/<int:id>', methods=['PUT'])
def update_claim(id):
    data = request.get_json()
    claim = Claim.query.get_or_404(id)
    claim.claim_number = data['claim_number']
    claim.claim_date = data['claim_date']
    claim.claim_amount = data['claim_amount']
    claim.claim_status = data['claim_status']
    claim.policy_id = data['policy_id']
    db.session.commit()
    return jsonify({'message': 'Claim updated'})

@main_blueprint.route('/claim/<int:id>', methods=['DELETE'])
def delete_claim(id):
    claim = Claim.query.get_or_404(id)
    db.session.delete(claim)
    db.session.commit()
    return jsonify({'message': 'Claim deleted'})

# Advanced data retrieval and reporting
@main_blueprint.route('/policy/<int:id>/claims', methods=['GET'])
def get_policy_claims(id):
    claims = Claim.query.filter_by(policy_id=id).all()
    return jsonify([
        {
            'claim_number': claim.claim_number,
            'claim_date': claim.claim_date,
            'claim_amount': claim.claim_amount,
            'claim_status': claim.claim_status
        } for claim in claims
    ])

@main_blueprint.route('/claims/report', methods=['GET'])
def get_claims_report():
    total_claims = db.session.query(db.func.count(Claim.id)).scalar()
    total_claim_amount = db.session.query(db.func.sum(Claim.claim_amount)).scalar()
    report = {
        'total_claims': total_claims,
        'total_claim_amount': total_claim_amount
    }
    return jsonify(report)


