import torch
from ultralytics import YOLO

model = YOLO("yolo11s.pt")

#Enables gpu if found
device = 0 if torch.cuda.is_available() else "cpu"
print("Using device:", device)

results = model("images/train/shortDrive.mp4", save=True, show = True, device=device)