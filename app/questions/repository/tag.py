from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.questions.models import Tag


def get_all(db: Session):
    return "get_all"
    tags = db.query(Tag).all()
    return tags

def questions_by_tag(id: int, db: Session):
    return "questions_by_tag"
    _tag = db.query(Tag).filter(Tag.id == id).first()
    if not _tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Tag with the id {id} is not available")
    return _tag