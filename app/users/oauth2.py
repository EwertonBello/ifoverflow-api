from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.users import token, repository
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(data: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = token.verify_token(data, credentials_exception)

    user = repository.user.get_by_email(token_data.email, db)
    if user is None:
        raise credentials_exception
    return user

async def get_current_user_or_none(data: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = token.verify_token(data, credentials_exception)

    user = repository.user.get_by_email(token_data.email, db)
    return user
