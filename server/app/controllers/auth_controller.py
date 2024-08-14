from flask import jsonify, request
from app.services.auth_service import login_user, register_user

def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    profile_photo = data.get('profile_photo', None)
    online_status = data.get('online_status', False) 

    response, status_code = register_user(username, password, profile_photo, online_status)
    return jsonify(response), status_code

def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    response, status_code = login_user(username, password)
    return jsonify(response), status_code