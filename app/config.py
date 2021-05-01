from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str
    secret_key: str
    mysql_database: str = "my_db"
    mysql_host: str = "localhost"
    mysql_username: str = "root"
    mysql_root_password: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

@lru_cache()
def get_settings():
    return Settings()
