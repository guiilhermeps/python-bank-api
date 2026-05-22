from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..database import get_db
from ..models.account import Account
from ..auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


class LoginRequest(BaseModel):
    account_id: int


@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == request.account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    token = create_access_token({"sub": str(account.id)})
    return {"access_token": token, "token_type": "bearer"}
