import re

from fastapi_users import schemas
from pydantic import BaseModel, validator


class AdditionalUserData(BaseModel):
    phone_number: str
    role: str

    @validator('phone_number')
    def validate_phone_number(cls, phone_number):
        pattern = r'^[78]\d{10}$'  # Паттерн: первый символ 7 или 8, затем 10 цифр
        if not re.match(pattern, phone_number):
            raise ValueError('Неверный формат номера телефона')
        return phone_number


class UserRead(schemas.BaseUser[int], AdditionalUserData):
    pass


class UserCreate(schemas.BaseUserCreate, AdditionalUserData):
    pass


class UserUpdate(schemas.BaseUserUpdate, AdditionalUserData):
    pass
