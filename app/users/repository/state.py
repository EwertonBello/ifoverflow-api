from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.users.models import State


def get_all(db: Session):
    states = db.query(State).all()
    return states

def show(id: int, db: Session):
    _state = db.query(State).filter(State.id == id).first()
    if not _state:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"State with the id {id} is not available")
    return _state

def campus_by_state(id: int, db: Session):
    campus_list = db.query(State.campus).filter(State.id == id)
    print(campus_list)
    return campus_list
