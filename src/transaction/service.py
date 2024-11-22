from sqlalchemy.ext.asyncio import AsyncSession

from .repository import TransactionRepository
from .schema import TransactionCreate, TransactionResponse


class TransactionService:
    @staticmethod
    async def create_transaction(
        data: TransactionCreate, bank_id: int, user_id: int, db: AsyncSession
    ) -> TransactionResponse:
        transaction_data = data.model_dump()
        transaction_data["user_id"] = user_id
        transaction_data["bank_id"] = bank_id
        transaction = await TransactionRepository.create_transaction(
            transaction_data, db
        )
        return TransactionResponse.model_validate(transaction)

    @staticmethod
    async def get_transactions_by_bank(
        bank_id: int, user_id: int, db: AsyncSession
    ) -> list[TransactionResponse]:
        transactions = await TransactionRepository.get_transactions_by_bank(
            bank_id, user_id, db
        )
        return [TransactionResponse.model_validate(t) for t in transactions]
