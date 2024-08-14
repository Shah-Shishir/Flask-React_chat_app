from app.models import db, User
from flask_jwt_extended import create_access_token

def register_user(username, password, profile_photo, online_status):
    if not username and not password:
        return {'message': 'Username and password required'}, 400
    elif not username:
        return {'message': 'Username required'}, 400
    elif not password:
        return {'message': 'Password required'}, 400

    try:
        user = User.query.filter_by(username=username).first()
        if user:
            return {'message': 'User already exists'}, 400
        
        new_user = User(username=username, profile_photo=profile_photo, online_status=online_status)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
    
    except ValueError as ve:
        return {'message': str(ve)}, 400

    return {'message': 'User registered successfully', 'new_user': new_user.to_dict()}, 201

def login_user(username, password):
    if not username or not password:
        return {'message': 'Username and password required'}, 400
    
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity={'username': username})
        return {'access_token': access_token}, 200
    
    return {'message': 'Invalid credentials'}, 401