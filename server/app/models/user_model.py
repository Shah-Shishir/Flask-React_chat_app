from datetime import datetime
import re
from app.models import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    profile_photo = db.Column(db.String(200), default=None)
    online_status = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.String(25), default=datetime.utcnow().isoformat())

    def validate_password(self, password):
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if not re.search(r'[@$!%*?&_]', password):
            return False
        return True

    def set_password(self, password):
        if not self.validate_password(password):
            raise ValueError("Password does not meet all the requirements")
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password_hash': self.password_hash,  
            'profile_photo': self.profile_photo,
            'online_status': self.online_status,
            'created_at': self.created_at,
        }