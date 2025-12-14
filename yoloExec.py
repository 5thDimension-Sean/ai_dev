from ultralytics import YOLO

model = YOLO("yolo11n.pt")
results = model("image.jpg")
results[0].show()