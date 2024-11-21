from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.user.models import User


class UserRepository:
    @staticmethod
    async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
        query = select(User).where(User.email == email)
        result = await session.execute(query)
        return result.scalars().first()

    @staticmethod
    async def create_user(
        session: AsyncSession, email: str, password_hash: str, name: str | None = None
    ) -> User:
        new_user = User(email=email, password_hash=password_hash, name=name)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user
