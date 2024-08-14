from flask import jsonify
from flask_jwt_extended import JWTManager
from flask_jwt_extended.exceptions import NoAuthorizationError
from werkzeug.exceptions import HTTPException

jwt = JWTManager()

@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({
        "error": "Authentication required",
        "message": "You need to provide a valid token to access this resource."
    }), 401

@jwt.invalid_token_loader
def invalid_token_response(callback):
    return jsonify({
        "error": "Invalid token",
        "message": "The token provided is invalid."
    }), 401

@jwt.expired_token_loader
def expired_token_response(jwt_header, jwt_payload):
    return jsonify({
        "error": "Expired token",
        "message": "The token has expired. Please login again."
    }), 401