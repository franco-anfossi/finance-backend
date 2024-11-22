from datetime import datetime

from pydantic import BaseModel, Field

from .enums import TransactionType


class TransactionCreate(BaseModel):
    type: TransactionType
    amount: float = Field(..., gt=0, description="Amount of the transaction")
    description: str | None = None


class TransactionResponse(BaseModel):
    id: int
    bank_id: int
    user_id: int
    type: TransactionType
    amount: float
    date: datetime
    description: str | None = None

    model_config = {"from_attributes": True}
