from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app import database

router = APIRouter(
    prefix="/campus",
    tags=['Campus']
)

get_db = database.get_db

@router.get('/')
def get_campus_list(db: Session = Depends(get_db)):
    return f"List of Campus"

@router.get('/{id}')
def get_campus(id: int, db: Session = Depends(get_db)):
    return f"Campus {id}"

@router.get('/{id}/users')
def get_users_by_campus(id: int, db: Session = Depends(get_db)):
    return f"Users of campus {id}"
