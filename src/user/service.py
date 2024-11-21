from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from src.user.repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    async def create_user(
        session: AsyncSession, email: str, password: str, name: str | None = None
    ):
        password_hash = UserService.hash_password(password)
        return await UserRepository.create_user(session, email, password_hash, name)

    @staticmethod
    async def authenticate_user(
        session: AsyncSession, email: str, password: str
    ) -> bool:
        user = await UserRepository.get_user_by_email(session, email)
        if not user:
            return False
        return pwd_context.verify(password, user.password_hash)
