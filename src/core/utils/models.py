from typing import Annotated

from pydantic import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import mapped_column


class ErrorModel(BaseModel):
    detail: str | dict[str, str]


# Primary key INT
IntPk = Annotated[int, mapped_column(primary_key=True)]

# VarChar 256
Str256 = Annotated[str, mapped_column(String(256))]
