from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.users.repository import user
from app import database

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

get_db = database.get_db


@router.post('/')
def register_user(request, db: Session = Depends(get_db)):
    return user.register(request, db)

@router.get('/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

@router.get('/profile/')
def get_profile(db: Session = Depends(get_db)):
    current_user = 1
    return user.show(current_user, db)