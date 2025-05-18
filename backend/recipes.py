from fastapi import APIRouter, Depends, HTTPException
from models import DishIn, DishOut
from db import get_collection
from bson.objectid import ObjectId

router = APIRouter()

@router.post("/api/add-dish", response_model=DishOut)
def add_dish(payload: DishIn):
    col = get_collection("dishes")
    result = col.insert_one(payload.dict())
    return DishOut(id=str(result.inserted_id), **payload.dict())
