from fastapi import APIRouter
from typing import List
from models import Order
from datetime import datetime

router = APIRouter()

@router.get("/api/orders", response_model=List[Order])
def get_orders():
    # 👉 Replace with real DB query later.
    demo = [
        Order(id="1001", customerName="Aditi", status="Delivered", total=450.0),
        Order(id="1002", customerName="Rohan", status="Preparing", total=299.0),
    ]
    return demo
