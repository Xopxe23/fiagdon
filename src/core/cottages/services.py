from fastapi import Depends, HTTPException

from src.core.cottages.repositories import CottageRepository, get_cottage_db
from src.core.cottages.schemas import CottageCreate, CottageRead


class CottageService:

    def __init__(
            self,
            cottage_db: CottageRepository
    ):
        self.cottage_db = cottage_db

    async def get_all(self) -> list[CottageRead]:
        result = await self.cottage_db.get_all()
        return result

    async def create(self, user_id: int, cottage_create: CottageCreate) -> CottageRead | HTTPException:
        create_dict = cottage_create.model_dump()
        create_dict["owner"] = user_id
        result = await self.cottage_db.create(create_dict)
        return result


async def get_cottage_service(cottage_db=Depends(get_cottage_db)):
    yield CottageService(cottage_db)
