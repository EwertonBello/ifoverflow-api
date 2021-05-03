from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
# from app.questions.repository import tag
# from app.questions.schemas import ShowTag, ShowTagWithQuestions
from app import database

router = APIRouter(
    prefix="/tags",
    tags=['Tags']
)

get_db = database.get_db

@router.get('/')
async def get_tags(db: Session = Depends(get_db)):
    return "tag.get_all(db)"

@router.get('/{id}/questions')
async def get_questions_by_tag(id: int, db: Session = Depends(get_db)):
    return "tag.questions_by_tag(id, db)"
