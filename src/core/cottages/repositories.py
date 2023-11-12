from fastapi import Depends
from sqlalchemy import and_, delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.cottages.models import Cottage
from src.core.cottages.schemas import CottageRead
from src.database import get_async_session


class CottageRepository:

    def __init__(
            self,
            session: AsyncSession,
            cottage_table: Cottage
    ):
        self.session = session
        self.cottage_table = cottage_table

    async def get_all(self, **filter_by) -> list[CottageRead]:
        query = select(Cottage).filter_by(**filter_by)
        result = await self.session.execute(query)
        result = [row[0].to_read_model() for row in result.all()]
        return result

    async def create(self, create_dict: dict) -> CottageRead:
        statement = insert(Cottage).values(**create_dict).returning(Cottage)
        result = await self.session.execute(statement)
        await self.session.commit()
        return result.scalar_one().to_read_model()

    async def get_by_id(self, cottage_id: int) -> CottageRead | None:
        query = select(Cottage).where(Cottage.id == cottage_id)
        result = await self.session.execute(query)
        result = result.scalar_one_or_none()
        if result is not None:
            return result.to_read_model()
        return result

    async def update(self, user_id: int, cottage_id: int, update_dict: dict) -> CottageRead:
        statement = update(Cottage).where(and_(
            Cottage.owner == user_id,
            Cottage.id == cottage_id
        )).values(**update_dict).returning(Cottage)
        result = await self.session.execute(statement)
        await self.session.commit()
        return result.scalar_one().to_read_model()

    async def delete(self, user_id: int, cottage_id: int):
        statement = delete(Cottage).where(and_(
            Cottage.owner == user_id,
            Cottage.id == cottage_id
        )).returning(Cottage.id)
        result = await self.session.execute(statement)
        await self.session.commit()
        return result.scalar_one()


async def get_cottage_db(session: AsyncSession = Depends(get_async_session)):
    yield CottageRepository(session, Cottage)
