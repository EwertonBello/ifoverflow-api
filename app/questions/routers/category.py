from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
# from app.questions.repository import category
# from app.questions.schemas import ShowCategory, ShowCategoryWithQuestions
from app import database

router = APIRouter(
    prefix="/states",
    tags=['States']
)

get_db = database.get_db

@router.get('/')
async def get_states(db: Session = Depends(get_db)):
    return "category.get_all(db)"

@router.get('/{id}')
async def get_state(id: int, db: Session = Depends(get_db)):
    return "category.show(id, db)"

@router.get('/{id}/campus')
async def get_campus_by_state(id: int, db: Session = Depends(get_db)):
    return "category.campus_by_state(id, db)"

