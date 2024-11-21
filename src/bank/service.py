from sqlalchemy.ext.asyncio import AsyncSession

from src.bank.repository import BankRepository
from src.bank.schema import BankCreate, BankResponse
from src.utils.security import encrypt_password


class BankService:
    @staticmethod
    async def create_bank(
        data: BankCreate, user_id: int, db: AsyncSession
    ) -> BankResponse:
        """
        Crear un nuevo banco para un usuario específico.
        """
        encrypted_password = encrypt_password(data.password)

        bank_data = {
            "user_id": user_id,
            "name": data.name,
            "username": data.username,
            "encrypted_password": encrypted_password,
            "additional_data": data.additional_data,
        }

        bank = await BankRepository.create_bank(bank_data, db)

        return BankResponse.model_validate(bank)

    @staticmethod
    async def get_banks_for_user(user_id: int, db: AsyncSession) -> list[BankResponse]:
        """
        Obtener todos los bancos asociados a un usuario.
        """
        banks = await BankRepository.get_banks_by_user_id(user_id, db)
        return [BankResponse.model_validate(bank) for bank in banks]
