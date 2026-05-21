from fastapi import FastAPI
from .controllers.transactions import router as transaction_router
from .controllers.accounts import router as account_router

app = FastAPI(prefix="/api/v1")
app.include_router(transaction_router, tags=["Transactions"])
app.include_router(account_router, tags=["Accounts"])

@app.get("/health")
def health_check():
    return {"status": "ok"}

