from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from app.routes.main_routes import main_routes
    from app.routes.auth_routes import auth_routes
    from app.routes.meeting_routes import meeting_routes
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(meeting_routes)

    return app