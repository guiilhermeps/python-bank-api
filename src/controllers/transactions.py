from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.account import Account
from ..models.transaction import Transaction
from ..schemas.transactions import TransactionRequest, TransactionResponse
from ..auth import get_current_user

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/deposit", response_model=TransactionResponse, status_code=201)
def create_deposit(request: TransactionRequest, db: Session = Depends(get_db), _=Depends(get_current_user)):
    account = db.query(Account).filter(Account.id == request.account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    account.balance += request.amount
    transaction = Transaction(account_id=account.id, type="deposit", amount=request.amount)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


@router.post("/withdrawal", response_model=TransactionResponse, status_code=201)
def create_withdrawal(request: TransactionRequest, db: Session = Depends(get_db), _=Depends(get_current_user)):
    account = db.query(Account).filter(Account.id == request.account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if account.balance < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    account.balance -= request.amount
    transaction = Transaction(account_id=account.id, type="withdrawal", amount=request.amount)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction
