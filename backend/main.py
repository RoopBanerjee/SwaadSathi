from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from auth import router as auth_router

app = FastAPI()

# Add your frontend URLs here
origins = [
    "http://localhost:3000",         # React local dev
    "http://127.0.0.1:3000",         # Alternate local
    "https://your-deployed-url.com" # Replace with your frontend deploy URL
]

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session middleware
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")  # Use a strong secret key

# Routers
app.include_router(auth_router)
