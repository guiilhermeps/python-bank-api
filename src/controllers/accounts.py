from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..database import get_db
from ..models.account import Account
from ..schemas.accounts import CreateAccountRequest, AccountResponse
import uuid

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/", response_model=AccountResponse, status_code=201)
async def create_account(request: CreateAccountRequest, db: AsyncSession = Depends(get_db)):
    account = Account(
        full_name=request.full_name,
        account_number=f"ACC-{uuid.uuid4().hex[:8].upper()}",
        balance=request.initial_deposit,
    )
    db.add(account)
    await db.commit()
    await db.refresh(account)
    return account


@router.get("/{account_id}", response_model=AccountResponse)
async def get_account(account_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Account).where(Account.id == account_id))
    account = result.scalar_one_or_none()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account
