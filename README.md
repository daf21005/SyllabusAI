# SyllabusAI - Student Academic Planning Tool

SyllabusAI is a student planning tool built to help students whose Universities uses Blackbord to track grades, calculate GPA, and make informed decisions about whether to drop or stay in a course. It combines a FastAPI backend with a Streamlit frontend to display courses, grades, GPA information, and assignment timelines in a single dashboard. It also includes syllabus upload and AI-based grading scal parsing via Google Gemini

__This project is used for portfolio and resume purposes only.__ It is not a finished product and is actively being developed. You may run a presentable version that uses old code at the directory ```final/```.

---

## Current State

### Backend (`backend/`)
The backend has been fully restructured and its core functionalities are working:
- All REST API endpoints are operational and tested
- SQLite database is connected and persisting data correctly
- Google Gemini AI integration is working - pases syllabus PDFs and text to extract grading scales
- Blackboard REST API OAuth2 integration is written but requires real institutional credentials to activate
- Mock data is used in place of live Blackboard data

__Note:__ The database has no authentication or access proection implemented. All endpoints are publicly accessible. This is ententianal for demonstation purposes.

### Frontend (`frontend/`)
The frontend Streamlit app is functional as apresentable demo but it is not fully connected to the restructed backend. The `final/` directory contains the version used for demos.


### Blackboard Integration
The Blackboard API functions are fully written but require real `BB_APP_KEY` and `BB_APP_SECRET` credentials from the [Anthology Developer Portal](https://developer.blackboard.com). Without these, the app runs on mock student and course data.

---

## Project Structure

```
SyllabusAI/
├── backend/              <- restructured backend (active development)
│   ├── main.py           <- FastAPI entry point
│   ├── database.py       <- SQLite connection and CRUD functions
│   ├── mock_data.py      <- mock student, course, and grade data
│   ├── blackboard.py     <- Blackboard API functions (needs credentials)
│   ├── routes/           <- API endpoint definitions
│   │   ├── courses.py
│   │   ├── grades.py
│   │   └── syllabus.py
│   ├── services/         <- business logic
│   │   ├── gemini_service.py
│   │   ├── gpa_service.py
│   │   └── blackboard_service.py
│   ├── models/           <- Pydantic data models
│   │   └── schemas.py
│   └── middleware/       <- authentication (not yet implemented)
│       └── auth.py
├── frontend/             <- Streamlit frontend (partner's work)
├── final/                <- presentable demo version
└── old/                  <- earlier iterations kept for reference
```

## Running the Demo Version (`final/`)
The `final/` directory is the stable demo version used for presentations.

### Prerequisites
- Python 3.10+
- `pip`

## 1) Set up a virtual environment (from repo root)
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 2) Install dependencies
```bash
python -m pip install -r final/backend/requirements.txt
python -m pip install -r final/frontend/requirements.txt
```

### 3) Add environment variables
Create a `.env` file inside `final/backend/`:
```env
GEMINI_API_KEY=your_key_here
```
If this key is missing, all pages still load but AI syllabus parsing will not work.

### 4) Run the backend (Terminal 1)
```bash
cd final/backend
python -m uvicorn main:app --reload --port 8000
```
Backend should be available at: `http://127.0.0.1:8000`

### 5) Run the frontend (Terminal 2)
```bash
cd final/frontend
python -m streamlit run app.py --server.port 8501
```
Frontend should be available at: `http://localhost:8501`

---

## Running the Active Backend (`backend/`)

The restructured backend can be tested via FastAPI's built-in interactive API docs at `http://localhost:8000/docs`
### Prerequisites
- Python 3.10+
- `.env` file inside `backend/` with your Gemini API key

### 1) Activate virtual environment
```bash
cd backend
source ../.venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run the backend
```bash
python -m uvicorn main:app --reload --port 8000
```

### 4) Open API docs
```
http://localhost:8000/docs
```

### Available Endpoints
```
GET  /                                    Health check
GET  /api/student                         Returns mock student info
GET  /api/courses/{student_id}            Returns courses with assignments
GET  /api/courses/{course_id}/recommendation  Drop or stay recommendation
GET  /api/grades/{student_id}             Returns letter grades per course
GET  /api/gpa                             Calculates current GPA
POST /api/upload/{course_id}              Upload syllabus PDF — Gemini extracts grading scale
POST /api/syllabus/parse/{course_id}      Paste syllabus text — Gemini extracts grading scale
```

---

## Known Limitations

- No authentication or API key protection on any endpoint
- Blackboard integration requires real institutional credentials
- Database uses SQLite — not suitable for multi-user production use
- Frontend is not yet connected to the restructured backend
- Google Gemini free tier may experience high demand errors (503) during peak hours

---

## References

- [Blackboard Learn REST API](https://developer.blackboard.com/portal/displayApi)
- [Google Gemini API](https://ai.google.dev/gemini-api/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
