from dataclasses import dataclass
from typing import Annotated

from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.core.cottages.schemas import CottageRead
from src.core.cottages.utils import CottageOptions
from src.core.utils.models import IntPk, Str256
from src.database import Base


class Cottage(Base):
    __tablename__ = 'cottages'

    id: Mapped[IntPk]
    owner: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    address: Mapped[Str256]
    lattitude: Mapped[float]
    longitude: Mapped[float]
    options: Mapped[CottageOptions]

    def to_read_model(self) -> CottageRead:
        return CottageRead(
            id=self.id,
            owner=self.owner,
            address=self.address,
            lattitude=self.lattitude,
            longitude=self.longitude,
            options=self.options
        )
