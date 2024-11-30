from pydantic import BaseModel

# Схема для создания пользователя
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Схема для ответа пользователя
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

