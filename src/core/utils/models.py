from typing import Annotated

from sqlalchemy import JSON, String
from sqlalchemy.orm import mapped_column

# Primary key INT
IntPk = Annotated[int, mapped_column(primary_key=True)]

# VarChar 256
Str256 = Annotated[str, mapped_column(String(256))]
