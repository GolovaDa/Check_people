
from ultralytics import YOLO

model = YOLO("models/yolo26s.pt")
result=model.predict(classes=[0],source=r"C:\Users\danil\people_counter_learning\examples\photo_2026-11-21_03-46-14.jpg")
result[0].show()
boxes=result[0].boxes.xyxy.tolist()

people_counts=len(result[0].boxes)
