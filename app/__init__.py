from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.routes.auth_routes import auth_bp
from app.routes.item_routes import item_bp
from app.config import Config
from app.models import db
from app.error_handlers.jwt_error_handlers import jwt, unauthorized_response, invalid_token_response, expired_token_response

def create_app():
    # Initialzie app
    app = Flask(__name__)

    # Configurations
    app.config.from_object(Config)

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    migrate = Migrate(app, db)

    # Initialize JWTManager with the app
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(item_bp, url_prefix='/api')

    # Register error handlers
    jwt.unauthorized_loader(unauthorized_response)
    jwt.invalid_token_loader(invalid_token_response)
    jwt.expired_token_loader(expired_token_response)

    return app
