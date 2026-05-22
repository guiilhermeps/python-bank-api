from fastapi import FastAPI
from .database import engine, Base
from .models import Account, Transaction
from .controllers.accounts import router as account_router
from .controllers.transactions import router as transaction_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bank API")
app.include_router(account_router, prefix="/api/v1")
app.include_router(transaction_router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok"}
