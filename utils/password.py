from passlib.hash import sha256_crypt

def hash_password(password):
    """Hash a password for storing."""
    password = sha256_crypt.encrypt(password)
    return password

 
def verify_password(password, stored_password):
    """Verify a stored password against one provided by user"""
    return sha256_crypt.verify(password, stored_password)