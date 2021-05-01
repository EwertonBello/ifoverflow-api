from fastapi import FastAPI
from app.database import engine, Base

from app.users.routers import user as users_user
from app.users.routers import campus as users_campus

from app.config import get_settings


app = FastAPI(title=get_settings().app_name)

app.include_router(users_user.router)
app.include_router(users_campus.router)
