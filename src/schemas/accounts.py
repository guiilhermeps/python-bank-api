from pydantic import BaseModel
from datetime import datetime


class CreateAccountRequest(BaseModel):
    full_name: str
    initial_deposit: float = 0.0


class AccountResponse(BaseModel):
    id: int
    full_name: str
    account_number: str
    balance: float
    created_at: datetime

    class Config:
        from_attributes = True
