from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.questions.repository import category
from app.questions.schemas import ShowCategory, ShowCategoryWithQuestions
from app import database

router = APIRouter(
    prefix="/categories",
    tags=['Categories']
)

get_db = database.get_db

@router.get('/', response_model=List[ShowCategory])
async def get_categories(db: Session = Depends(get_db)):
    return category.get_all(db)

@router.get('/{id}', response_model=ShowCategory)
async def get_category(id: int, db: Session = Depends(get_db)):
    return category.show(id, db)

@router.get('/{id}/questions', response_model=ShowCategoryWithQuestions)
async def get_questions_by_category(id: int, db: Session = Depends(get_db)):
    return category.questions_by_category(id, db)

