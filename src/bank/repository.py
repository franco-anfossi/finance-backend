from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.bank.models import Bank


class BankRepository:
    @staticmethod
    async def create_bank(data: dict, db: AsyncSession) -> Bank:
        """
        Inserta un nuevo banco en la base de datos.
        """
        new_bank = Bank(**data)
        db.add(new_bank)
        await db.commit()
        await db.refresh(new_bank)
        return new_bank

    @staticmethod
    async def get_banks_by_user_id(user_id: int, db: AsyncSession) -> list[Bank]:
        """
        Obtiene todos los bancos asociados a un usuario específico.
        """
        query = select(Bank).where(Bank.user_id == user_id)
        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_bank_by_id(
        bank_id: int, user_id: int, db: AsyncSession
    ) -> Bank | None:
        """
        Obtiene un banco por su ID y valida que pertenezca al usuario.
        """
        query = select(Bank).where(Bank.id == bank_id, Bank.user_id == user_id)
        result = await db.execute(query)
        return result.scalars().first()

    @staticmethod
    async def update_bank(bank_id: int, data: dict, db: AsyncSession) -> Bank | None:
        """
        Actualiza un banco existente.
        """
        query = (
            update(Bank)
            .where(Bank.id == bank_id)
            .values(**data)
            .execution_options(synchronize_session="fetch")
        )
        await db.execute(query)
        await db.commit()
        query = select(Bank).where(Bank.id == bank_id)
        result = await db.execute(query)
        return result.scalars().first()

    @staticmethod
    async def delete_bank(bank_id: int, user_id: int, db: AsyncSession) -> None:
        """
        Elimina un banco por su ID y usuario.
        """
        query = select(Bank).where(Bank.id == bank_id, Bank.user_id == user_id)
        result = await db.execute(query)
        bank_to_delete = result.scalars().first()

        if bank_to_delete:
            await db.delete(bank_to_delete)
            await db.commit()
