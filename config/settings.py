from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Supabase
    supabase_url: str
    supabase_key: str
    
    # App
    base_url: str = "http://localhost:8000"
    
    class Config:
        env_file = ".env"

settings = Settings()