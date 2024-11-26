import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env файла

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./test.db')
