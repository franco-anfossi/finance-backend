from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .enums import SupportedBanks


class BankCreate(BaseModel):
    name: SupportedBanks
    username: str = Field(
        ..., max_length=255, description="Username for accessing the bank"
    )
    password: str = Field(..., description="Raw password for the bank account")
    additional_data: Optional[dict] = Field(
        None, description="Any additional data like OTP info or keys"
    )


class BankUpdate(BaseModel):
    name: Optional[SupportedBanks] = None
    username: Optional[str] = Field(None, max_length=255)
    password: Optional[str] = None
    additional_data: Optional[dict] = None


class BankResponse(BaseModel):
    id: int
    name: SupportedBanks
    username: str
    additional_data: Optional[dict] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

    def __init__(self, **data):
        super().__init__(**data)
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
