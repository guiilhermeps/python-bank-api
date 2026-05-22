from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..database import get_db
from ..models.account import Account
from ..models.transaction import Transaction
from ..schemas.transactions import TransactionRequest, TransactionResponse
from ..auth import get_current_user

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/deposit", response_model=TransactionResponse, status_code=201)
async def create_deposit(request: TransactionRequest, db: AsyncSession = Depends(get_db), _=Depends(get_current_user)):
    result = await db.execute(select(Account).where(Account.id == request.account_id))
    account = result.scalar_one_or_none()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    account.balance += request.amount
    transaction = Transaction(account_id=account.id, type="deposit", amount=request.amount)
    db.add(transaction)
    await db.commit()
    await db.refresh(transaction)
    return transaction


@router.post("/withdrawal", response_model=TransactionResponse, status_code=201)
async def create_withdrawal(request: TransactionRequest, db: AsyncSession = Depends(get_db), _=Depends(get_current_user)):
    result = await db.execute(select(Account).where(Account.id == request.account_id))
    account = result.scalar_one_or_none()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if account.balance < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    account.balance -= request.amount
    transaction = Transaction(account_id=account.id, type="withdrawal", amount=request.amount)
    db.add(transaction)
    await db.commit()
    await db.refresh(transaction)
    return transaction
