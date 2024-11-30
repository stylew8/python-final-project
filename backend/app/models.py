from app.database import Base
from sqlalchemy import (
    Column, Integer, String, ForeignKey, Date, Float, Text, Table
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Person(Base):
    __abstract__ = True 
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    salt = Column(String(255), nullable=False)

class Admin(Person):
    __tablename__ = "admins"
    pass


# Students Table
class Student(Person):
    __tablename__ = "students"
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")

# Teachers Table
class Teacher(Person):
    __tablename__ = "teachers"
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    subjects = relationship("Subject", back_populates="teacher")

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    group = relationship("Group", back_populates="subjects")
    semester_id = Column(Integer, ForeignKey("semesters.id"), nullable=False)
    semester = relationship("Semester", back_populates="subjects")
    grade_types = relationship("GradeType", back_populates="subject")  # Связь с GradeType
    teacher = relationship("Teacher", back_populates="subjects", uselist=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=True)

# Groups Table
class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    study_program_id = Column(Integer, ForeignKey("study_programs.id"), nullable=False)
    study_program = relationship("StudyProgram", back_populates="groups")
    students = relationship("Student", back_populates="group")
    subjects = relationship("Subject", back_populates="group")

# StudyPrograms Table
class StudyProgram(Base):
    __tablename__ = "study_programs"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    groups = relationship("Group", back_populates="study_program")
    study_plans = relationship("StudyPlan", back_populates="study_program")  # Связь с StudyPlan


# StudyPlans Table
class StudyPlan(Base):
    __tablename__ = "study_plans"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    program_id = Column(Integer, ForeignKey("study_programs.id"), nullable=False)
    study_program = relationship("StudyProgram", back_populates="study_plans")  # Связь с StudyProgram
    semesters = relationship("Semester", back_populates="study_plan")


# StudyPlanSubjects Table (Связь между учебным планом и предметами)
class StudyPlanSubject(Base):
    __tablename__ = "study_plan_subjects"
    id = Column(Integer, primary_key=True)
    study_plan_id = Column(Integer, ForeignKey("study_plans.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)

# Subjects Table


class GradeType(Base):
    __tablename__ = "grade_types"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)  # Например, "PD", "KN", "EG"
    description = Column(Text, nullable=True)  # Описание типа оценки
    percentage = Column(Float, nullable=False)  # Процент влияния на итоговый балл
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)  # Связь с предметом
    subject = relationship("Subject", back_populates="grade_types")
    grades = relationship("Grade", back_populates="grade_type")

# Оценки
class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)  # Значение оценки
    grade_type_id = Column(Integer, ForeignKey("grade_types.id"), nullable=False)  # Связь с GradeType
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)  # Связь со студентом
    final_grade = Column(Float, nullable=True)  # Итоговая оценка (если есть)
    grade_type = relationship("GradeType", back_populates="grades")
    student = relationship("Student", back_populates="grades")

# Semesters Table
class Semester(Base):
    __tablename__ = "semesters"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)  # Название семестра, например "Fall 2024"
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    study_plan_id = Column(Integer, ForeignKey("study_plans.id"), nullable=False)
    study_plan = relationship("StudyPlan", back_populates="semesters")
    subjects = relationship("Subject", back_populates="semester")
