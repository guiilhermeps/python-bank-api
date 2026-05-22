from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.account import Account
from ..schemas.accounts import CreateAccountRequest, AccountResponse
import uuid

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/", response_model=AccountResponse, status_code=201)
def create_account(request: CreateAccountRequest, db: Session = Depends(get_db)):
    account = Account(
        full_name=request.full_name,
        account_number=f"ACC-{uuid.uuid4().hex[:8].upper()}",
        balance=request.initial_deposit,
    )
    db.add(account)
    db.commit()
    db.refresh(account)
    return account


@router.get("/{account_id}", response_model=AccountResponse)
def get_account(account_id: int, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account
