from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import Transaction


class TransactionRepository:
    @staticmethod
    async def create_transaction(data: dict, db: AsyncSession) -> Transaction:
        transaction = Transaction(**data)
        db.add(transaction)
        await db.commit()
        await db.refresh(transaction)
        return transaction

    @staticmethod
    async def get_transactions_by_user(
        user_id: int, db: AsyncSession
    ) -> list[Transaction]:
        query = select(Transaction).where(Transaction.user_id == user_id)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_transactions_by_bank(
        bank_id: int, user_id: int, db: AsyncSession
    ) -> list[Transaction]:
        """
        Filtra transacciones por banco y usuario.
        """
        query = select(Transaction).where(
            Transaction.bank_id == bank_id, Transaction.user_id == user_id
        )
        result = await db.execute(query)
        return result.scalars().all()
