import torch
print(torch.cuda.is_available()) # Check for GPU availability

from ultralytics import YOLO
import boto3
print(boto3.__version__)


'''
model = YOLO("yolo11s.pt")
model.train(data="coco128.yaml",epochs=3,imgsz=1280,name="yolo11n-results",device=0)
model.val(data="coco128.yaml",imgsz=1280,device=0)
results = model("images/train/trafficLight.jpg", save=True, project="runs", name="predict")
results[0].show()
print(results[0].save_dir)

model.export(format="onnx", dynamic=True)
'''