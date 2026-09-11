MOCK_STUDENT = {"id": 1, "name": "John", "blackboard_id": "student_001"}

MOCK_COURSES = [
    {
        "id":1,
        "course_name": "Calculus III",
        "credits": 4,
        "current_grade": 88.5,
        "assignments": [
            {"name": "HW 1",    "start_date": "2026-01-20", "due_date": "2026-01-27", "weight_pct": 5,  "type": "Homework"},
            {"name": "HW 2",    "start_date": "2026-02-03", "due_date": "2026-02-10", "weight_pct": 5,  "type": "Homework"},
            {"name": "Quiz 1",  "start_date": "2026-02-14", "due_date": "2026-02-14", "weight_pct": 5,  "type": "Quiz"},
            {"name": "Midterm", "start_date": "2026-03-08", "due_date": "2026-03-10", "weight_pct": 30, "type": "Exam"},
            {"name": "HW 3",    "start_date": "2026-03-17", "due_date": "2026-03-24", "weight_pct": 5,  "type": "Homework"},
            {"name": "Project", "start_date": "2026-04-01", "due_date": "2026-04-18", "weight_pct": 20, "type": "Project"},
            {"name": "Final",   "start_date": "2026-05-03", "due_date": "2026-05-05", "weight_pct": 30, "type": "Exam"},
        ],
    },
    {
        "id":2,
        "course_name": "Cybersecurity",
        "credits": 3,
        "current_grade": 64.0,
        "assignments": [
            {"name": "Lab 1",   "start_date": "2026-01-22", "due_date": "2026-01-29", "weight_pct": 10, "type": "Lab"},
            {"name": "Lab 2",   "start_date": "2026-02-12", "due_date": "2026-02-19", "weight_pct": 10, "type": "Lab"},
            {"name": "Midterm", "start_date": "2026-03-11", "due_date": "2026-03-13", "weight_pct": 25, "type": "Exam"},
            {"name": "Lab 3",   "start_date": "2026-04-02", "due_date": "2026-04-09", "weight_pct": 15, "type": "Lab"},
            {"name": "Final",   "start_date": "2026-05-06", "due_date": "2026-05-08", "weight_pct": 40, "type": "Exam"},
        ],
    },
    {
        "id":3,
        "course_name": "Systems Programming",
        "credits": 3,
        "current_grade": 91.2,
        "assignments": [
            {"name": "HW 1",    "start_date": "2026-01-27", "due_date": "2026-02-03", "weight_pct": 8,  "type": "Homework"},
            {"name": "HW 2",    "start_date": "2026-02-17", "due_date": "2026-02-24", "weight_pct": 8,  "type": "Homework"},
            {"name": "Midterm", "start_date": "2026-03-14", "due_date": "2026-03-16", "weight_pct": 29, "type": "Exam"},
            {"name": "HW 3",    "start_date": "2026-03-30", "due_date": "2026-04-06", "weight_pct": 8,  "type": "Homework"},
            {"name": "Project", "start_date": "2026-04-07", "due_date": "2026-04-28", "weight_pct": 17, "type": "Project"},
            {"name": "Final",   "start_date": "2026-05-09", "due_date": "2026-05-11", "weight_pct": 30, "type": "Exam"},
        ],
    },
    {
        "id":4,
        "course_name": "Linear Algebra",
        "credits": 3,
        "current_grade": 73.5,
        "assignments": [
            {"name": "HW 1",    "start_date": "2026-01-21", "due_date": "2026-01-28", "weight_pct": 10, "type": "Homework"},
            {"name": "Quiz 1",  "start_date": "2026-02-11", "due_date": "2026-02-11", "weight_pct": 5,  "type": "Quiz"},
            {"name": "Midterm", "start_date": "2026-03-09", "due_date": "2026-03-11", "weight_pct": 35, "type": "Exam"},
            {"name": "HW 2",    "start_date": "2026-04-01", "due_date": "2026-04-08", "weight_pct": 10, "type": "Homework"},
            {"name": "Final",   "start_date": "2026-05-07", "due_date": "2026-05-09", "weight_pct": 40, "type": "Exam"},
        ],
    },
]

MOCK_GRADES = [
    {"course": "Calculus III",      "grade": "B+", "gpa": 3.3, "semester": "Spring 2026"},
    {"course": "Cybersecurity",     "grade": "D",  "gpa": 1.3, "semester": "Spring 2026"},
    {"course": "Systems Programming","grade": "A", "gpa": 4.0, "semester": "Spring 2026"},
    {"course": "Linear Algebra",    "grade": "C",  "gpa": 2.0, "semester": "Spring 2026"},
]

"""
Use this grading scale for reference when parsing syllabi with Gemini. The AI model may return inconsistent formats, so ensure the output matches expected letter grades and percentage thresholds.
Grading Scale: A: 93-100, A-: 90-92, B+: 87-89, B: 83-86, B-: 80-82, C+: 77-79, C: 73-76, C-: 70-72, D: 60-69, F: below 60
"""