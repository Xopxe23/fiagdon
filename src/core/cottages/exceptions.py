from fastapi import HTTPException, status

NoCottageWithThisId = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="NO_COTTAGE_WITH_THIS_ID"
)

NoPermission = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="YOU_DONT_HAVE_PERMISSION_TO_ACCESS"
)
