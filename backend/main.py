from fastapi import FastAPI, HTTPException
from auth import create_user, delete_user

app = FastAPI()

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
