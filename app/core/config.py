from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My FastAPI App"
    admin_email: str = "admin@example.com"
    items_per_user: int = 50

    class Config:
        env_file = ".env"

settings = Settings()
