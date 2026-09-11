from database import save_course_weights
from fastapi import APIRouter, File, HTTPException, UploadFile
from models.schemas import SyllabusText
from services.gemini_service import parse_syllabus_pdf, parse_syllabus_text

router = APIRouter()

# allows the student to upload the syllabus to obtain the grade scales
@router.post("/api/upload/{course_id}")
async def upload_syllabus(file: UploadFile = File(...), course_id: int = None):
    # validate file is a PDF
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are accepted"
         )

    contents = await file.read()

    try:
        # using Gemini to scan the PDF
        result = parse_syllabus_pdf(contents)

        for entry in result.get("grading_scale", []):
             save_course_weights(
                  # ISSUE FIXED - this was hardcoded where the course ID was equal to 1
                  course_id=course_id,
                  category=entry["letter"],
                  weight_percentage=entry["max_pct"],
                  current_score=entry["min_pct"]
             )

        return {
            "status": "success",
            "filename": file.filename,
            "course_id": course_id,
            "result": result
        }

    except ValueError as e:
         raise HTTPException(status_code=500, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


# allows to the student to maunally type the grading scales
@router.post("/api/syllabus/parse/{course_id}")
async def parse_syllabus(payload: SyllabusText, course_id: int):
    try: 
        result = parse_syllabus_text(payload.text)
        for entry in result.get("grading_scale", []):
                    save_course_weights(
                        # ISSUE FIXED - same one as above ^
                        course_id=course_id,
                        category=entry["letter"],
                        weight_percentage=entry["max_pct"],
                        current_score=entry["min_pct"]
                    )
        
        return {
            "status": "success",
            "course_id": course_id,
            "result": result
            }
    
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))