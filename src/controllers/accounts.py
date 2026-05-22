from fastapi import APIRouter
from ..schemas.accounts import AccountsSchema
from datetime import datetime

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.post("/create")
def create_account(fullname: str, initial_deposit: float = 0.0):
    #TODO Add logic to create an account into database. It can be a public endpoint
    # if fullname is None or fullname.strip() == "":
        

    return {"message": "Account created successfully"}

@router.get("/{account_id}", response_model=AccountsSchema)
def get_account(account_id: int):
    return {
        "id": account_id,
        "full_name": "John Doe",
        "account_number": f"ACC-{account_id}",
        "balance": 1000.0,
        "created_at": datetime.now().isoformat()
    }