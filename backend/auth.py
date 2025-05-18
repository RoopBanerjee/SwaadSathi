from fastapi import APIRouter, Request, HTTPException
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials, initialize_app
from db import save_user_to_db
import os

# Initialize Firebase Admin
if not firebase_auth._apps:
    cred_path = os.getenv("FIREBASE_ADMIN_CRED", "firebase_admin_credentials.json")
    cred = credentials.Certificate(cred_path)
    initialize_app(cred)

router = APIRouter()

@router.post("/login")
async def login(request: Request):
    body = await request.json()
    id_token = body.get("idToken")
    if not id_token:
        raise HTTPException(status_code=400, detail="Missing ID token")

    try:
        decoded_token = firebase_auth.verify_id_token(id_token)
        uid = decoded_token["uid"]
        email = decoded_token.get("email", "")
        name = decoded_token.get("name", "")

        request.session["uid"] = uid  # Store UID in session

        # Save user to MongoDB
        user_data = {
            "uid": uid,
            "email": email,
            "name": name
        }
        save_user_to_db(user_data)

        return {"message": "Login successful", "uid": uid, "email": email, "name": name}
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")

@router.get("/verify-session")
async def verify_session(request: Request):
    uid = request.session.get("uid")
    if not uid:
        raise HTTPException(status_code=401, detail="Not logged in")
    return {"message": "Session valid", "uid": uid}

@router.post("/logout")
async def logout(request: Request):
    request.session.clear()
    return {"message": "Logged out"}
