from werkzeug.security import safe_str_cmp
from models.user import User
from utils.password import verify_password

def authenticate(email, password):
    user = User.query.filter_by(email=email).first()

    if user:
        
        password_accurate = verify_password(password, user.password)
        
        if password_accurate:
            return user

def identity(payload):
    user_id = payload['identity']
    return User.query.filter(User.id == payload['identity']).scalar()
