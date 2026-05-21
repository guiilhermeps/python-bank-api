from fastapi import APIRouter

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.post("/create")
def create_account():
    return {"message": "Account created successfully"}

@router.get("/{account_id}")
def get_account(account_id: int):
    return {"account_id": account_id}