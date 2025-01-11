import hashlib
import os

# A simple mock database of users
users_db = {}

def create_user(username, password):
    # Hash the password before storing it
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users_db[username] = hashed_password

def authenticate_user(username, password):
    # Check if the user exists and the password matches
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in users_db and users_db[username] == hashed_password:
        return True
    return False

# Example usage
create_user("john_doe", "password123")
is_authenticated = authenticate_user("john_doe", "password123")
