from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def get_all(db: Session):
    return "Repository: List of States"

def show(id: int, db: Session):
    return f"Repository: State {id}"

def campus_by_state(id: int, db: Session):
    return f"Repository: List Campus of state {id}"
