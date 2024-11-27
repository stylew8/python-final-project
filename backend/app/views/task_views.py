from fastapi import APIRouter, Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.views.auth_views import verify_token_function
from app.database import get_db
from app.models import Student, Semester, StudyPlan

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
