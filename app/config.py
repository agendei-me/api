from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str
