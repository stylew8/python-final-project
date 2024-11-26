from fastapi import APIRouter, Depends
from .models import User
from .auth import token_required
from .schemas import UserCreate, UserResponse

api_router = APIRouter()

@api_router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate):
    # Логика регистрации пользователя
    new_user = User(username=user.username, email=user.email, hashed_password=user.password)
    new_user.save()
    return new_user

@api_router.get("/users", response_model=list[UserResponse])
def get_users(current_user: User = Depends(token_required)):
    # Только авторизованные пользователи могут видеть список всех пользователей
    users = User.query.all()
    return users
