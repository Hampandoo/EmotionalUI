from ai.recognizeImage.main import recognizeEmotions
from app.schemas.recognize import RecognizeRequest
import cv2
import numpy as np
import base64

class RecognizeService:
  def recognizeEmotions(self, base64Image):
    image_data = base64.b64decode(base64Image.split(',')[1])
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    emotions = recognizeEmotions(img)
    return emotions

  def convert_types(self, obj):
    if isinstance(obj, np.ndarray):
      return obj.tolist()
    elif isinstance(obj, np.generic):
      return obj.item() 
    elif isinstance(obj, dict):
      return {k: self.convert_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
      return [self.convert_types(v) for v in obj]
    return obj