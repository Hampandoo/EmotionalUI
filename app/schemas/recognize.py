from pydantic import BaseModel

class RecognizeRequest(BaseModel):
  base64Image: str

class EmotionSchema(BaseModel):
  happy: str
  angry: str
class RecognizeResponse(BaseModel):
  emotion: EmotionSchema