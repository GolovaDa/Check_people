
from ultralytics import YOLO

model = YOLO("models/yolo26s.pt")

def detect_people(image):

    result=model.predict(classes=[0],source=image)
    
    boxes=result[0].boxes.xyxy.tolist()
    return boxes
