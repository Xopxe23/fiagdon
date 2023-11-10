from fastapi import Depends
from sqlalchemy import insert, select
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


async def get_cottage_db(session: AsyncSession = Depends(get_async_session)):
    yield CottageRepository(session, Cottage)
