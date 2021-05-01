from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import get_settings

_database_name = get_settings().mysql_database
_host = get_settings().mysql_host
_user = get_settings().mysql_username
_password = get_settings().mysql_root_password

SQLALCHEMY_DATABASE_URL = f"mysql://{_user}:{_password}@{_host}/{_database_name}?charset=utf8"


engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding="utf-8")

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
