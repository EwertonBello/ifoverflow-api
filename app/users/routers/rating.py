from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app import database

router = APIRouter(
    prefix="/ratings",
    tags=['Ratings']
)

get_db = database.get_db

@router.get('/')
async def get_ratings(db: Session = Depends(get_db)):
    return f"List of Ratings"

@router.get('/{id}')
async def get_rating(id: int, db: Session = Depends(get_db)):
    return f"Rating {id}"

@router.get('/{id}/users')
async def get_users_by_rating(id: int, db: Session = Depends(get_db)):
    return f"Users of rating {id}"

# NÃO SERÁ UTILIZADO AINDA
