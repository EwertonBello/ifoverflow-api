from sqlalchemy.orm import Session
from app.users import models, schemas
from fastapi import HTTPException, status
# from app.users.hashing import Hash


def register(request: schemas.User, db: Session):
    return new_user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user
