'''
must create conda environment with pyhton 3.9 with dependencies installed:
ultralytics
pytorch quick setup 
'''
from ultralytics import YOLO

#sample model from ultralytics website
model = YOLO("yolov8n.pt")

model.predict(source=0, save=True, conf=0.5, show=True)
