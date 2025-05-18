# ai_recipe.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import random

router = APIRouter()

class RecipeRequest(BaseModel):
    ingredients: list[str]

@router.post("/generate-recipe")
def generate_recipe(data: RecipeRequest):
    if not data.ingredients:
        raise HTTPException(status_code=400, detail="No ingredients provided.")
    
    # Dummy response (replace with OpenAI later if needed)
    recipe = {
        "title": f"{random.choice(data.ingredients).capitalize()} Special",
        "ingredients": data.ingredients,
        "instructions": f"Mix {', '.join(data.ingredients)} and cook for 20 mins."
    }
    return recipe
