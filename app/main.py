from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base

from app.users.routers import state as users_state
from app.users.routers import campus as users_campus
from app.users.routers import user as users_user
from app.users.routers import authentication as users_authentication
from app.questions.routers import category as questions_category
from app.questions.routers import tag as questions_tag
from app.questions.routers import question as questions_question
from app.answers.routers import answer as answers_answer
from app.comments.routers import comment as comments_comment

from app.config import get_settings


app = FastAPI(title=get_settings().app_name)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_state.router)
app.include_router(users_campus.router)
app.include_router(users_user.router)
app.include_router(users_authentication.router)
app.include_router(questions_category.router)
app.include_router(questions_tag.router)
app.include_router(questions_question.router)
app.include_router(answers_answer.router)
app.include_router(comments_comment.router)
