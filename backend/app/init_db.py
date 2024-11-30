import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Semester, StudyPlan, StudyProgram, Admin, Student, Teacher, Group, Subject, GradeType, Grade
from dotenv import load_dotenv
from passlib.context import CryptContext

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Загрузка переменных окружения
load_dotenv()

# Настройка подключения к базе данных
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str, salt: str) -> str:
    """Хэширование пароля с солью."""
    return pwd_context.hash(password + salt)

def init_db():
    """Инициализация базы данных."""
    # Создание таблиц
    Base.metadata.create_all(bind=engine)

    # Хэшированный пароль
    salt = "73LP05Z853OX568H0ZMRG78Y"
    password = "123"
    hashed_password = hash_password(password, salt)

    # Создание учебной программы
    study_program = StudyProgram(
        name="Computer Science",
        description="Program for computer science students."
    )
    db.add(study_program)
    db.commit()

    # Создание группы
    group = Group(
        name="CS-101",
        study_program_id=study_program.id
    )
    db.add(group)
    db.commit()

    # Создание учебного плана
    study_plan = StudyPlan(
        name="CS Basic Plan",
        program_id=study_program.id
    )
    db.add(study_plan)
    db.commit()

    # Создание семестра
    semester = Semester(
        name="Spring 2024",
        start_date="2024-01-01",
        end_date="2024-06-01",
        study_plan_id=study_plan.id
    )
    db.add(semester)
    db.commit()

    # Создание предмета
    subject = Subject(
        name="Introduction to Programming",
        description="Basic programming course.",
        group_id=group.id,
        semester_id=semester.id,
        teacher_id=None
    )
    db.add(subject)
    db.commit()

    # Создание типов оценок
    grade_types = [
        GradeType(name="PD", description="Практическое задание", percentage=20.0, subject_id=subject.id),
        GradeType(name="KN", description="Контрольная работа", percentage=30.0, subject_id=subject.id),
        GradeType(name="EG", description="Экзамен", percentage=50.0, subject_id=subject.id)
    ]
    db.add_all(grade_types)
    db.commit()

    # Создание студента
    student = Student(
        username="student",
        hashed_password=hashed_password,
        salt=salt,
        first_name="John",
        last_name="Doe",
        group_id=group.id
    )
    db.add(student)
    db.commit()

    # Создание оценок
    grades = [
        Grade(value=9.0, grade_type_id=grade_types[0].id, student_id=student.id),
        Grade(value=8.5, grade_type_id=grade_types[1].id, student_id=student.id),
        Grade(value=10.0, grade_type_id=grade_types[2].id, student_id=student.id)
    ]
    db.add_all(grades)
    db.commit()

    # Создание администратора
    admin = Admin(
        username="admin",
        hashed_password=hashed_password,
        salt=salt
    )
    db.add(admin)
    db.commit()

    # Создание учителя
    teacher = Teacher(
        username="teacher",
        hashed_password=hashed_password,
        salt=salt,
        first_name="Jane",
        last_name="Smith"
    )
    db.add(teacher)
    db.commit()

    # Назначение учителя предмету
    subject.teacher_id = teacher.id
    db.commit()

    print("База данных успешно инициализирована!")

# Запуск скрипта
if __name__ == "__main__":
    init_db()
