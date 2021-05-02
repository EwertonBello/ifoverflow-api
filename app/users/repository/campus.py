from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def get_all(db: Session):
    return "Repository: List of Campus"

def show(id: int, db: Session):
    return f"Repository: Campus {id}"

def users_by_campus(id: int, db: Session):
    return f"Repository: Users of campus {id}"
