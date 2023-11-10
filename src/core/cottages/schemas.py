from pydantic import BaseModel

from src.core.cottages.utils import Options


class CottageRead(BaseModel):
    id: int
    owner: int
    address: str
    lattitude: float
    longitude: float
    options: Options


# Pydantic схема для создания
class CottageCreate(BaseModel):
    address: str
    lattitude: float
    longitude: float
    options: Options

    class Config:
        from_attributes = True
