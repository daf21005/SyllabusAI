from contextlib import asynccontextmanager

from database import init_db, save_student
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mock_data import MOCK_STUDENT
from routes.courses import router as courses_router
from routes.grades import router as grades_router
from routes.syllabus import router as syllabus_router

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="SyllabusAI Backend", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",
        "http://localhost:5173",
        "http://127.0.0.1:8501",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ENDPOINTS
app.include_router(courses_router)
app.include_router(grades_router)
app.include_router(syllabus_router)

@app.get("/")
def root():
    return {"message": "SyllabusAI backend is running"}

@app.get("/api/student")
def get_student_endpoint():
    save_student(
        MOCK_STUDENT["name"], MOCK_STUDENT["blackboard_id"]
    )
    return MOCK_STUDENT
