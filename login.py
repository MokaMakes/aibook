import hashlib
import getpass

# Simple user database (username: hashed_password)
users = {
    "admin": hashlib.sha256("password123".encode()).hexdigest(),
    "user1": hashlib.sha256("letmein".encode()).hexdigest()
}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username not in users:
        print("❌ User does not exist")
        return False

    if users[username] == hash_password(password):
        print("✅ Login successful!")
        return True
    else:
        print("❌ Incorrect password")
        return False

# Run login
login()
