from fastapi import Depends
from src.core.cottages.repositories import CottageRepository, get_cottage_db
from src.core.cottages.schemas import CottageCreate, CottageRead, CottageUpdate


class CottageService:

    def __init__(
            self,
            cottage_db: CottageRepository
    ):
        self.cottage_db = cottage_db

    async def get_all(self) -> list[CottageRead]:
        result = await self.cottage_db.get_all()
        return result

    async def create(self, user_id: int, cottage_create: CottageCreate) -> CottageRead:
        create_dict = cottage_create.model_dump()
        create_dict["owner"] = user_id
        result = await self.cottage_db.create(create_dict)
        return result

    async def get_by_id(self, cottage_id: int) -> CottageRead | None:
        result = await self.cottage_db.get_by_id(cottage_id)
        return result

    async def update(self, user_id: int, cottage_id: int,
                     cottage_update: CottageUpdate) -> CottageRead:
        update_dict = cottage_update.model_dump()
        result = await self.cottage_db.update(user_id, cottage_id, update_dict)
        return result

    async def delete(self, user_id: int, cottage_id: int) -> str:
        result = await self.cottage_db.delete(user_id, cottage_id)
        return f"Cottage with id: {result} deleted"


async def get_cottage_service(cottage_db=Depends(get_cottage_db)):
    yield CottageService(cottage_db)
