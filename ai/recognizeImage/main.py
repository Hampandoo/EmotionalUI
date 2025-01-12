from deepface import DeepFace
import sys

def recognizeEmotions(img_path):
    objs = DeepFace.analyze(
        img_path=img_path,
        actions=['age', 'gender', 'race', 'emotion']
    )

    return objs