"""
Definition of  Dependency get_current_user
"""

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
import token
from fastapi.security import OAuth2AuthorizationCodeBearer
from item import token

# to check the Token is valid or not
# where YOU want to fectch the Token(login route)
# FastAPI will fetch the token from the below path
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(data, credentials_exception)
