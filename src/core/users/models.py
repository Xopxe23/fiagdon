from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    phone_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
