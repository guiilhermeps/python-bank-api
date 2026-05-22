from pydantic import BaseModel, field_validator
from datetime import datetime


class TransactionRequest(BaseModel):
    account_id: int
    amount: float

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("amount must be greater than zero")
        return v


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    type: str
    amount: float
    created_at: datetime

    class Config:
        from_attributes = True
