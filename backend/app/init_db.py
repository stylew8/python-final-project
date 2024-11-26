import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base,Admin,User,Teacher,Subject,Class
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Строка подключения из .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Создаем движок SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Сессия для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Функция для инициализации базы данных
# Функция для инициализации базы данных
def init_db():
    # Создание всех таблиц в базе данных
    Base.metadata.create_all(bind=engine)

    # Проверим, есть ли уже данные в таблицах
    if not db.query(Subject).first():
        # Добавление предметов
        subjects = [
            Subject(name="Математика"),
            Subject(name="Литовский"),
            Subject(name="Информатика")
        ]
        db.add_all(subjects)
        db.commit()

    if not db.query(Class).first():
        # Добавление классов
        class_1A = Class(name="1A")
        db.add(class_1A)
        db.commit()

    if not db.query(Teacher).first():
        # Создание учителей и установка связи с классом
        class_1A = db.query(Class).filter_by(name="1A").first()  # Получаем класс
        teacher1 = Teacher(username="teacher1", email="teacher1@example.com", hashed_password="hashed_password_teacher")
        class_1A.teacher = teacher1  # Устанавливаем связь между классом и учителем
        db.add(teacher1)
        db.commit()

    if not db.query(User).first():
        # Добавление студентов
        student1 = User(username="student1", email="student1@example.com", hashed_password="hashed_password_student")
        student2 = User(username="student2", email="student2@example.com", hashed_password="hashed_password_student")
        db.add(student1)
        db.add(student2)
        db.commit()

        # Привязка студентов к классу
        class_1A.students.append(student1)
        class_1A.students.append(student2)
        db.commit()

    if not db.query(Admin).first():
        admin1 = Admin(username="adm", email="exmpl@gmail.com", hashed_password="hashed_password")

        db.add(admin1)
        db.commit()


    print("База данных успешно инициализирована!")


# Запуск инициализации базы данных
if __name__ == "__main__":
    init_db()
