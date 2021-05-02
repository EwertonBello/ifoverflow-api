from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.users.repository import user
from app.users.schemas import User, ShowUser, ShowProfile
from app import database

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=ShowUser)
def register_user(request: User, db: Session = Depends(get_db)):
    return user.register(request, db)

@router.get('/{id}', response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

@router.get('/profile/', response_model=ShowProfile)
def get_profile(db: Session = Depends(get_db)):
    current_user = 1
    return user.show(current_user, db)