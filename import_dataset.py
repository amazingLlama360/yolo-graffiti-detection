from roboflow import Roboflow
rf = Roboflow(api_key="OMe2jdQuTmjFj890mU16")
project = rf.workspace("suri-e5d1w").project("graff-ymab0-b0odn")
version = project.version(1)
dataset = version.download("yolov8")


