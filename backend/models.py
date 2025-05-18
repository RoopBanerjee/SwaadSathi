from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional


class SignUpBody(BaseModel):
    email: str
    password: str


class DishIn(BaseModel):
    name: str
    price: float = Field(..., gt=0)


class DishOut(DishIn):
    id: str


class Order(BaseModel):
    id: str
    customerName: str
    status: str
    total: float
    created_at: datetime = Field(default_factory=datetime.utcnow)


# You can add Expense, Nutrition, etc. later
