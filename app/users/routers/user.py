from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app import database

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

get_db = database.get_db


@router.post('/')
def register_user(request, db: Session = Depends(get_db)):
    return "CALL cadastrar user"

@router.get('/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    return f"User {id}"

@router.get('/profile')
def get_profile(db: Session = Depends(get_db)):
    return "My Profile"