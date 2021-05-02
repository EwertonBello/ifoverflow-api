from sqlalchemy.orm import Session
from app.users import models, schemas
from fastapi import HTTPException, status
from app.users.hashing import Hash


def register(request: schemas.User, db: Session):
    return new_user

def show(id: int, db: Session):
    return f"User by id {id}"
