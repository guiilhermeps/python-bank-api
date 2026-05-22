from pydantic import BaseModel
from datetime import datetime


class TransactionRequest(BaseModel):
    account_id: int
    amount: float


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    type: str
    amount: float
    created_at: datetime

    class Config:
        from_attributes = True
