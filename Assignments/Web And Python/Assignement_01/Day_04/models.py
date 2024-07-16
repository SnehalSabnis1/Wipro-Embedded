from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_number = db.Column(db.String(20), unique=True, nullable=False)
    policy_holder_name = db.Column(db.String(100), nullable=False)
    coverage_amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()