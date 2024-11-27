import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Semester, StudyPlan, StudyProgram
from dotenv import load_dotenv

from models import Admin, Student, Teacher, Group, Subject, Base



# Загружаем переменные окружения из .env
load_dotenv()

# Строка подключения из .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Создаем движок SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Сессия для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()


from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

hashed_password = pwd_context.hash("123")


def init_db():
    # Создаём все таблицы
    Base.metadata.create_all(bind=engine)

    # Фиксированные данные для хэширования паролей
    Salt = "73LP05Z853OX568H0ZMRG78Y"
    password = "123"
    hashedPassword = pwd_context.hash(password + Salt)

    # Добавляем фейковую учебную программу
    fake_study_program = StudyProgram(
        name="Fake Study Program",
        description="This is a placeholder study program."
    )
    db.add(fake_study_program)
    db.commit()

    # Добавляем фейковую группу, привязанную к учебной программе
    fake_group = Group(
        name="Fake Group",
        study_program_id=fake_study_program.id
    )
    db.add(fake_group)
    db.commit()

    # Добавляем фейковый учебный план, привязанный к учебной программе
    fake_study_plan = StudyPlan(
        name="Fake Study Plan",
        program_id=fake_study_program.id
    )
    db.add(fake_study_plan)
    db.commit()

    # Добавляем фейковый семестр, привязанный к учебному плану
    fake_semester = Semester(
        name="Fake Semester",
        start_date="2024-01-01",
        end_date="2024-06-01",
        study_plan_id=fake_study_plan.id
    )
    db.add(fake_semester)
    db.commit()

    # Добавляем фейковый предмет, привязанный к группе и семестру
    fake_subject = Subject(
        name="Fake Subject",
        description="This is a placeholder subject.",
        group_id=fake_group.id,
        semester_id=fake_semester.id
    )
    db.add(fake_subject)
    db.commit()

    # Добавляем администратора
    admin = Admin(
        username="admin",
        hashed_password=hashedPassword,
        salt=Salt
    )
    db.add(admin)
    db.commit()

    # Добавляем студента, привязанного к группе
    student = Student(
        username="student",
        hashed_password=hashedPassword,
        salt=Salt,
        first_name="John",
        last_name="Doe",
        group_id=fake_group.id
    )
    db.add(student)
    db.commit()

    # Добавляем учителя, привязанного к предмету
    teacher = Teacher(
        username="teacher",
        hashed_password=hashedPassword,
        salt=Salt,
        first_name="Jane",
        last_name="Smith",
        subject_id=fake_subject.id
    )
    db.add(teacher)
    db.commit()

    print("База данных успешно инициализирована с фейковыми данными!")



# Запуск инициализации базы данных
if __name__ == "__main__":
    init_db()
