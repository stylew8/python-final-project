from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

# Класс для предметов
class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)

    def __repr__(self):
        return f"<Subject(id={self.id}, name={self.name})>"

# Класс для классов
class Class(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)

    # Связь с учителем
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    # Связь с учениками (многие ко многим через таблицу students_classes)
    students = relationship('User', secondary='students_classes', back_populates='classes')
    teacher = relationship('Teacher', back_populates='classes')

    def __repr__(self):
        return f"<Class(id={self.id}, name={self.name})>"

# Связь многие ко многим между учениками и классами
class StudentsClasses(Base):
    __tablename__ = 'students_classes'

    student_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    class_id = Column(Integer, ForeignKey('classes.id'), primary_key=True)

# Класс для пользователей (студенты и учителя)
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))

    # Связь с классами
    classes = relationship('Class', secondary='students_classes', back_populates='students')

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"

# Класс для учителей
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))

    # Связь с классом
    classes = relationship('Class', back_populates='teacher', uselist=False)

    def __repr__(self):
        return f"<Teacher(id={self.id}, username={self.username})>"
    
class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))

    def __repr__(self):
        return f"<Admin(id={self.id}, username={self.username})>"

# Класс для домашних заданий
class Homework(Base):
    __tablename__ = 'homeworks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    due_date = Column(DateTime, default=datetime.utcnow)

    subject = relationship('Subject')

    def __repr__(self):
        return f"<Homework(id={self.id}, title={self.title}, due_date={self.due_date})>"

# Класс для оценок
class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, index=True)
    grade = Column(Integer)
    homework_id = Column(Integer, ForeignKey('homeworks.id'))
    student_id = Column(Integer, ForeignKey('users.id'))

    homework = relationship('Homework')
    student = relationship('User')

    def __repr__(self):
        return f"<Grade(id={self.id}, grade={self.grade}, homework_id={self.homework_id}, student_id={self.student_id})>"

