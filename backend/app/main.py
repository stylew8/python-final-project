# main.py
from fastapi import FastAPI
from app.views.auth_views import router as auth_router
from app.views.user_views import router as user_router
from app.views.teacher_views import router as teacher_router
from app.views.task_views import router as task_router
from app.views.admin_views import router as admin_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",  # Пример разрешенного источника
    "http://localhost:3000",  # Если ваш фронтенд на другом порту
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Разрешенные источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы
    allow_headers=["*"],  # Разрешить все заголовки
)

# Подключаем все роуты
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(teacher_router)
app.include_router(task_router)