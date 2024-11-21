from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.permissions import get_current_user
from src.database import get_db
from src.user.schema import UserCreate, UserResponse
from src.user.service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await UserService.authenticate_user(db, user.email, user.password)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )
    new_user = await UserService.create_user(db, user.email, user.password, user.name)
    return new_user


@router.get("/me")
async def get_me(current_user: int = Depends(get_current_user)):
    return {"user_id": current_user}
