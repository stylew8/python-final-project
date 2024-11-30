from fastapi import APIRouter, Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.views.auth_views import verify_token_function
from app.database import get_db
from app.models import Student, Semester, StudyPlan, Subject,Grade, GradeType, Teacher

from app.schemas.semester_schema import SemesterBase, SemesterList

router = APIRouter()

@router.get("/students/semesters")
def get_student_semesters(
    db: Session = Depends(get_db),
    payloads: str = Depends(verify_token_function)
    ):

    student_id = payloads["user_id"] 

    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    study_plan_ids = [plan.id for plan in student.group.study_program.study_plans]

    semesters = db.query(Semester).join(StudyPlan).filter(StudyPlan.id.in_(study_plan_ids)).all()

    return semesters

@router.get("/student/semester/info/{semester_id}")
def get_semester_info(
    semester_id: int,
    db: Session = Depends(get_db),
    payloads: str = Depends(verify_token_function)
    ):

    student_id = payloads["user_id"] 
    student = db.query(Student).filter(Student.id == student_id).first()

    subjects = db.query(Subject).filter(Subject.group_id == student.group_id,
                                         Subject.semester_id == semester_id).all()

    semester = db.query(Semester).filter(Semester.id == semester_id).first()

    return {"subjects": subjects,
            "semester_name": semester.name}


@router.get("/student/info/me")
def get_info_me(
    db: Session = Depends(get_db),
    payloads: str = Depends(verify_token_function)
    ):
    
    student_id = payloads["user_id"] 
    student = db.query(Student).filter(Student.id == student_id).first()



    return {"student_id": student.id,
            "full_name": student.first_name + student.last_name,
            "group_name": student.group.name,
            "program_name": student.group.study_program.name}



@router.get("/student/subject/{subject_id}")
def get_subject(subject_id: int, db: Session = Depends(get_db)):
    print(f"Fetching subject with ID: {subject_id}")  # Логирование
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return {"subject": subject, "teacher_name": {subject.teacher.first_name + " " + subject.teacher.last_name}, "grade_types":subject.grade_types}


@router.get("/student/grade/{grade_type_id}")
def get_grade(
    grade_type_id: int,
    db: Session = Depends(get_db),
    payloads: dict = Depends(verify_token_function)  # Предположим, что verify_token_function возвращает словарь
):
    student_id = payloads["user_id"]

    # Выполняем запрос и получаем первую запись
    grade = db.query(Grade).filter(
        Grade.grade_type_id == grade_type_id,
        Grade.student_id == student_id
    ).first()

    # Проверяем, найден ли результат
    if not grade:
        return {"grade": None} 

    # Возвращаем найденный результат в виде словаря
    return {
        "id": grade.id,
        "value": grade.value,
        "grade_type_id": grade.grade_type_id,
        "student_id": grade.student_id,
        "final_grade": grade.final_grade
    }

