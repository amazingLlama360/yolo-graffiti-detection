from ultralytics import YOLO

model = YOLO('best.pt')

results = model('graffiti_test_2.mp4', show=True, save=True, conf=0.5)

