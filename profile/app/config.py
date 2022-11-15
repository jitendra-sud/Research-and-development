from pydantic import BaseSettings,EmailStr


class Settings(BaseSettings):
    AWS_SECRET_ACCESS_KEY :str
    AWS_ACCESS_KEY_ID:str
    DATABASE_URL:str
    class Config:
        env_file = 'app/.env'


settings = Settings()
