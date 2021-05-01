from fastapi import FastAPI
from app.database import engine, Base

from app.users.routers import user
from app.config import get_settings


app = FastAPI(title=get_settings().app_name)

app.include_router(user.router)
