from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.questions.repository import question
from app.questions.schemas import ShowBaseQuestion, ShowQuestion, Question
from app.users.schemas import User
from app.users import oauth2
from app import database

router = APIRouter(
    prefix="/questions",
    tags=['Questions']
)

get_db = database.get_db

@router.post('/', status_code=201)
async def create_question(request: Question, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return question.create(current_user.id, request, db)

@router.get('/', response_model=List[ShowBaseQuestion])
async def get_questions(db: Session = Depends(get_db)):
    return question.get_all(db)

@router.get('/{id}', response_model=ShowQuestion)
async def get_question(id: int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user_or_none)):
    return question.show(current_user, id, db)

@router.get('/search/{query}', response_model=List[ShowBaseQuestion])
async def search_questions(query: str, db: Session = Depends(get_db)):
    return question.search(query, db)

@router.put('/{id}/positive')
async def vote_positive(id: int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return question.vote_question(True, current_user.id, id, db)

@router.put('/{id}/negative')
async def vote_negative(id: int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return question.vote_question(False, current_user.id, id, db)
