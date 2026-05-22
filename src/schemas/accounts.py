from pydantic import BaseModel, field_validator
from datetime import datetime


class CreateAccountRequest(BaseModel):
    full_name: str
    initial_deposit: float = 0.0

    @field_validator("full_name")
    @classmethod
    def name_not_empty(cls, v):
        if not v.strip():
            raise ValueError("full_name cannot be empty")
        return v.strip()


class AccountResponse(BaseModel):
    id: int
    full_name: str
    account_number: str
    balance: float
    created_at: datetime

    class Config:
        from_attributes = True
