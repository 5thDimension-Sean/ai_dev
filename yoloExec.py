from ultralytics import YOLO

'''
model = YOLO("yolo11n.pt")
model.train(data="coco128.yaml",epochs=3,imgsz=640,name="yolo11n-results",device=0)
model.val(data="coco128.yaml",imgsz=640,device=0)
results = model("images/train/trafficLight.jpg", save=True, project="runs", name="predict")
results[0].show()
print(results[0].save_dir)

model.export(format="onnx", dynamic=True)
'''

model = YOLO("yolo11n.pt")

results = model("images/train/shortDrive.mp4", save=True, show = True, device=0)