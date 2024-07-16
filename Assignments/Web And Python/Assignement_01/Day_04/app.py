from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Policy
from forms import PolicyForm
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)


    app.secret_key = app.config['SECRET_KEY']


    with app.app_context():
        db.create_all()


        # Policy list view
        @app.route('/')
        def policy_list():
            policies = Policy.query.all()
            return render_template('policy_list.html', policies=policies)


        # Policy detail view
        @app.route('/policy/<int:id>')
        def policy_detail(id):
            policy = Policy.query.get_or_404(id)
            return render_template('policy_detail.html', policy=policy)


        # Create or update policy view
        @app.route('/policy/edit', methods=['GET', 'POST'])
        @app.route('/policy/edit/<int:id>', methods=['GET', 'POST'])
        def policy_edit(id=None):
            if id:
                policy = Policy.query.get_or_404(id)
            else:
                policy = Policy()


            form = PolicyForm(obj=policy)
            if form.validate_on_submit():
                form.populate_obj(policy)
                policy.save()
                flash('Policy saved successfully.', 'success')
                return redirect(url_for('policy_list'))
            return render_template('policy_form.html', form=form, policy=policy)


    return app


if __name__ == '__main__':
    app = create_app()
    

    app.run(port=5001, debug=True)  # Start the application on port 5001 with debug mode enabled

