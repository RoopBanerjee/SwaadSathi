# diet.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class DietRequest(BaseModel):
    age: int
    weight: float
    gender: str  # "male" or "female"

@router.post("/recommend-diet")
def recommend_diet(data: DietRequest):
    calories = 2000
    if data.gender == "male":
        calories += 200
    if data.age < 18:
        calories -= 200
    elif data.age > 60:
        calories -= 100

    return {
        "recommended_calories": calories,
        "diet_plan": {
            "breakfast": "Oats + Milk + Fruits",
            "lunch": "Rice + Daal + Veggies",
            "dinner": "Chapati + Sabzi + Curd"
        }
    }
