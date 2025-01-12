from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.recognize import RecognizeRequest
from app.services.recognize_service import RecognizeService

router = APIRouter()

@router.post("/recognize")
def recognize(request_data: RecognizeRequest):
  img = request_data.base64Image
  try:
    emotions = RecognizeService().recognizeEmotions(img)
    emotions = RecognizeService().convert_types(emotions)

    return { "message": emotions }
  except Exception as e:
    error_response = {
      "error": "Error recognizion image",
      "detail": "Face could not be detected"
    }
    return JSONResponse(status_code=400, content=error_response)