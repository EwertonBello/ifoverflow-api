from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.users.repository import campus
from app import database

router = APIRouter(
    prefix="/campus",
    tags=['Campus']
)

get_db = database.get_db

@router.get('/')
def get_campus_list(db: Session = Depends(get_db)):
    return campus.get_all(db)

@router.get('/{id}')
def get_campus(id: int, db: Session = Depends(get_db)):
    return campus.show(id, db)

@router.get('/{id}/users')
def get_users_by_campus(id: int, db: Session = Depends(get_db)):
    return campus.users_by_campus(id, db)
