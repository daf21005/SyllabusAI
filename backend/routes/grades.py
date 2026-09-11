from database import get_student as db_get_student
from database import save_gpa_history
from fastapi import APIRouter
from mock_data import MOCK_COURSES, MOCK_GRADES
from services.gpa_service import calculate_gpa

router = APIRouter()

# get a list of all grades for a specific student
@router.get("/api/grades/{student_id}")
def get_grades(student_id: str):
    student = db_get_student(student_id)

    if student:
        for grade in MOCK_GRADES:
            save_gpa_history(
                student["id"], grade["semester"], grade["gpa"]
            )
    return MOCK_GRADES

# get the student's overall GPA
@router.get("/api/gpa")
def gpa_endpoint():
    return calculate_gpa(MOCK_COURSES)