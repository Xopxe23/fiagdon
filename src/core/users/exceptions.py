from fastapi import HTTPException, status

PhoneNumberAlreadyExists = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="USER_WITH_THIS_PHONE_NUMBER_ALREADY_EXISTS"
)
