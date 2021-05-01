from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app import database

router = APIRouter(
    prefix="/states",
    tags=['States']
)

get_db = database.get_db

@router.get('/')
def get_states(db: Session = Depends(get_db)):
    return f"List of States"

@router.get('/{id}')
def get_state(id: int, db: Session = Depends(get_db)):
    return f"State {id}"

@router.get('/{id}/campus')
def get_campus_by_state(id: int, db: Session = Depends(get_db)):
    return f"Campus of state {id}"
