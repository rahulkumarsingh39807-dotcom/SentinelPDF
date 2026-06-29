from flask import Flask
from flask_login import LoginManager

from config import Config
from models import db, User

from routes.dashboard import dashboard
from routes.auth import auth
from routes.analysis import analysis

# Create Flask app FIRST
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

# User loader
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# Register blueprints
app.register_blueprint(dashboard)
app.register_blueprint(auth)
app.register_blueprint(analysis)
# Create database tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)