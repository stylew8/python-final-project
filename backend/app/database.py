import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Строка подключения из .env
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Создаем объект Base для модели
Base = declarative_base()

# Создаем движок SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=3600)

# Сессия для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
