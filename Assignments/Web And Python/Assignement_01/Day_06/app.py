from flask import Flask
from config import Config
from models import db
from routes import main_blueprint

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
