import firebase_admin
from firebase_admin import auth, credentials

cred = credentials.Certificate("C:\\Users\\Abhijeet\\Desktop\\Project\\swaadsathi-2025-firebase-adminsdk-fbsvc-c20d63f0df.json")
firebase_admin.initialize_app(cred)

def create_user(email, password):
    user = auth.create_user(email=email, password=password)
    print(f"User created: {user.uid}")
    return user

def delete_user(uid):
    auth.delete_user(uid)
    print(f"User {uid} deleted")

def verify_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        print(f"Token verification failed: {e}")
        return None
