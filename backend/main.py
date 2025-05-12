from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from auth import create_user, delete_user, verify_token

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/signup")
async def signup(email: str, password: str):
    try:
        user = create_user(email, password)
        return {"message": "User created successfully!", "uid": user.uid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/delete_user/")
async def delete_user_api(uid: str):
    try:
        delete_user(uid)
        return {"message": f"User {uid} deleted successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/profile")
async def protected_route(request: Request):
    # Expect ID token in Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    id_token = auth_header.split("Bearer ")[-1]  # Format: Bearer <token>
    user_info = verify_token(id_token)
    if not user_info:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return {"message": "Token verified!", "user": user_info}
