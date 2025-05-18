# image_scan.py
from fastapi import APIRouter, File, UploadFile
import random

router = APIRouter()

@router.post("/scan-ingredients")
async def scan_ingredients(file: UploadFile = File(...)):
    # Dummy detection (replace with image recognition model later)
    possible_ingredients = ["tomato", "onion", "carrot", "potato", "spinach"]
    detected = random.sample(possible_ingredients, k=3)
    return {"detected_ingredients": detected}
