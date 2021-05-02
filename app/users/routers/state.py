from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.users.repository import state
from app import database

router = APIRouter(
    prefix="/states",
    tags=['States']
)

get_db = database.get_db

@router.get('/')
def get_states(db: Session = Depends(get_db)):
    return state.get_all(db)

@router.get('/{id}')
def get_state(id: int, db: Session = Depends(get_db)):
    return state.show(id, db)

@router.get('/{id}/campus')
def get_campus_by_state(id: int, db: Session = Depends(get_db)):
    return state.campus_by_state(id, db)
