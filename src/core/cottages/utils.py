from dataclasses import dataclass
from typing import Annotated

from sqlalchemy import JSON
from sqlalchemy.orm import mapped_column


# Options for cottage model
@dataclass
class Options:
    pool: bool
    parking: bool
    air_conditioning: bool
    wifi: bool


CottageOptions = Annotated[Options, mapped_column(
    JSON, default=Options(pool=False, parking=False, air_conditioning=False, wifi=False)
)]
