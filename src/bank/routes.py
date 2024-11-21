from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.permissions import get_current_user
from src.bank.repository import BankRepository
from src.bank.schema import BankCreate, BankResponse, BankUpdate
from src.bank.service import BankService
from src.database import get_db
from src.utils.security import encrypt_password

router = APIRouter(prefix="/banks", tags=["banks"])


@router.post("/", response_model=BankResponse, status_code=status.HTTP_201_CREATED)
async def create_bank(
    bank_data: BankCreate,
    db: AsyncSession = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    """
    Crea un nuevo banco para el usuario autenticado.
    """
    return await BankService.create_bank(bank_data, current_user, db)


@router.get("/", response_model=list[BankResponse], status_code=status.HTTP_200_OK)
async def list_banks(
    db: AsyncSession = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    """
    Lista todos los bancos del usuario autenticado.
    """
    return await BankService.get_banks_for_user(current_user, db)


@router.get("/{bank_id}", response_model=BankResponse, status_code=status.HTTP_200_OK)
async def get_bank(
    bank_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    """
    Obtiene un banco específico por su ID si pertenece al usuario autenticado.
    """
    bank = await BankRepository.get_bank_by_id(bank_id, current_user, db)
    if not bank:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Bank not found"
        )
    return BankResponse.model_validate(bank)


@router.patch("/{bank_id}", response_model=BankResponse, status_code=status.HTTP_200_OK)
async def update_bank(
    bank_id: int,
    bank_data: BankUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    """
    Actualiza un banco específico si pertenece al usuario autenticado.
    """
    update_data = bank_data.model_dump(exclude_unset=True)

    if "password" in update_data:
        update_data["encrypted_password"] = encrypt_password(
            update_data.pop("password")
        )

    bank = await BankRepository.update_bank(bank_id, update_data, db)
    if not bank:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Bank not found"
        )
    return BankResponse.model_validate(bank)


@router.delete("/{bank_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bank(
    bank_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    """
    Elimina un banco específico si pertenece al usuario autenticado.
    """
    await BankRepository.delete_bank(bank_id, current_user, db)

    return None
