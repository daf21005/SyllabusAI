from database import get_student as db_get_student
from database import save_course
from fastapi import APIRouter, HTTPException
from mock_data import MOCK_COURSES

router = APIRouter()

# get a list of all courses for a specific student
@router.get("/api/courses/{student_id}")
def get_courses(student_id: str):
    student = db_get_student(student_id)

    if student:
        for course in MOCK_COURSES:
            save_course(
                student["id"], course["course_name"], course["credits"], course["current_grade"]
            )
    return MOCK_COURSES

# get a recommendation for a specific course
@router.get("/api/courses/{course_id}/recommendation")
def get_recommendation(course_id: int):
    course = next((c for c in MOCK_COURSES if c.get("id") == course_id), None)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    grade = course["current_grade"]
    if grade >= 70:
        return {"course_name": course["course_name"], "current_grade": grade,
                "recommendation": "Stay",
                "reason": f"Your grade of {grade}% is passing. You can recover from here."}
    return {"course_name": course["course_name"], "current_grade": grade,
            "recommendation": "Consider Dropping",
            "reason": f"Your grade of {grade}% is below 70%. Dropping protects your GPA."}
