from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.users import models, schemas
from app.users.hashing import Hash


def register(request: schemas.User, db: Session):
    request.password=Hash.bcrypt(request.password)
    new_user = request.dict()
    try:
        db.execute(
            text('CALL cadastrarUsuario(:name, :avatar, :email, :password, :campus_id)'), 
            new_user)
        db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="User not created, check the request body and try again")

    return HTTPException(status_code=status.HTTP_201_CREATED,
                            detail=f"User {request.name} created successfully!")

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user

def get_by_email(email: str, db: Session):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the email {email} is not available")
    return user
