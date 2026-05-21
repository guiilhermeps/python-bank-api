from fastapi import APIRouter
import sqlite3

router = APIRouter()
conn = sqlite3.connect('bank.db')

@router.post("/transaction/withdrawal")
def create_withdrawal_transaction():
    pass

@router.post("/transaction/deposit")
def create_deposit_transaction():
    pass

@router.get("/transactions")
def get_transactions():
    pass

