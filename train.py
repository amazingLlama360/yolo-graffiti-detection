from ultralytics import YOLO

model = YOLO('yolov8n.pt')

model.train(
    data='/Users/alanliu/Desktop/Code/AV&CompVision_Projects/graffiti_yolo/Graff-1/data.yaml',
    epochs=50,
    imgsz=640
)