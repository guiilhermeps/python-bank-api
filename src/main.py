from contextlib import asynccontextmanager
from fastapi import FastAPI
from .database import engine, Base
from .models import Account, Transaction
from .controllers.accounts import router as account_router
from .controllers.transactions import router as transaction_router
from .controllers.auth import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Bank API", lifespan=lifespan)
app.include_router(account_router, prefix="/api/v1")
app.include_router(transaction_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
