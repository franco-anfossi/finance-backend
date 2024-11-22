from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.transaction.schema import TransactionCreate, TransactionResponse
from src.transaction.service import TransactionService

from ..auth.permissions import get_current_user

router = APIRouter(prefix="/banks/{bank_id}/transactions", tags=["transactions"])


@router.post(
    "/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED
)
async def create_transaction(
    bank_id: int,
    transaction: TransactionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    return await TransactionService.create_transaction(
        transaction, bank_id, current_user, db
    )


@router.get(
    "/", response_model=list[TransactionResponse], status_code=status.HTTP_200_OK
)
async def list_transactions(
    bank_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    return await TransactionService.get_transactions_by_bank(bank_id, current_user, db)
