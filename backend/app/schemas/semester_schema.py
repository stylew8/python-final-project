from pydantic import BaseModel
from typing import List
from datetime import date

class SemesterBase(BaseModel):
    id: int
    name: str
    duration: str
    start_date: str  # Используем строковый тип
    end_date: str    # Используем строковый тип

    class Config:
        from_attributes = True  # Это нужно для сериализации SQLAlchemy моделей


class SemesterList(BaseModel):
    semesters: List[SemesterBase]  # Список семестров

    class Config:
        from_attributes = True  # Нужно для сериализации списка
