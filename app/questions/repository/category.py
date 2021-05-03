from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.questions.models import Category


def get_all(db: Session):
    return "get_all"
    categories = db.query(Category).all()
    return categories

def show(id: int, db: Session):
    return "show"
    _category = db.query(Category).filter(Category.id == id).first()
    if not _category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Category with the id {id} is not available")
    return _category

def questions_by_category(id: int, db: Session):
    return "questions_by_category"
    _category = db.query(Category).filter(Category.id == id).first()
    if not _category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Category with the id {id} is not available")
    return _category
