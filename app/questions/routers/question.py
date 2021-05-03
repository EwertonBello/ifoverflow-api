from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.questions.repository import question
from app.questions.schemas import ShowBaseQuestion, ShowQuestion, Question
from app import database

router = APIRouter(
    prefix="/questions",
    tags=['Questions']
)

get_db = database.get_db

@router.post('/', status_code=201)
async def create_question(request: Question, db: Session = Depends(get_db)):
    return question.create(request, db)

@router.get('/', response_model=List[ShowBaseQuestion])
async def get_questions(db: Session = Depends(get_db)):
    return question.get_all(db)

@router.get('/{id}', response_model=ShowQuestion)
async def get_question(id: int, db: Session = Depends(get_db)):
    return question.show(id, db)

# @router.get('/{query}', response_model=List[ShowBaseQuestion])
@router.get('/search/{query}')
async def search_questions(query: str, db: Session = Depends(get_db)):
    return question.search(query, db)

@router.put('/{id}')
async def vote_question(id: int, db: Session = Depends(get_db)):
    return question.vote_question(id, db)
