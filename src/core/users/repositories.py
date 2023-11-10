from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.users.models import User
from src.core.users.schemas import UserRead
from src.database import get_async_session


class UserRepository(SQLAlchemyUserDatabase):
    async def get_by_phone_number(self, phone_number: str) -> UserRead | None:
        statement = select(self.user_table).where(self.user_table.phone_number == phone_number)
        return await self._get_user(statement)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield UserRepository(session, User)
