# expense.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

expenses_db = []

class Expense(BaseModel):
    name: str
    amount: float
    date: str  # YYYY-MM-DD

@router.post("/add-expense")
def add_expense(data: Expense):
    expenses_db.append(data.dict())
    return {"message": "Expense added successfully."}

@router.get("/total-expense")
def total_expense():
    total = sum(item['amount'] for item in expenses_db)
    return {"total_expense": total, "entries": expenses_db}
