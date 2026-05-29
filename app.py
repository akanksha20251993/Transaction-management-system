from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Transaction Model
class Transaction(BaseModel):
    transaction_id: int
    merchant: str
    amount: float

# Home API
@app.get("/")
def home():
    return {"message": "Payment Intelligence System Running"}

# Fraud Detection API
@app.post("/transaction")
def create_transaction(transaction: Transaction):

    risk = "Low"

    if transaction.amount > 10000:
        risk = "High"

    return {
        "transaction_id": transaction.transaction_id,
        "merchant": transaction.merchant,
        "amount": transaction.amount,
        "risk": risk
    }
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:shalu@localhost/payments_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()