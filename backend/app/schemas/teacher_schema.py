from pydantic import BaseModel

# Схема для создания пользователя
class TeacherCreate(BaseModel):
    username: str
    email: str
    password: str

# Схема для ответа пользователя
class TeacherResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True
