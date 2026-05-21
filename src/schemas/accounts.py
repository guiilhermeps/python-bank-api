from pydantic import BaseModel

class AccountsSchema(BaseModel):
    id: int
    full_name: str
    account_number: str
    balance: float | None = None
    created_at: str

