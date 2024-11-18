from ultralytics import YOLO

# Charger le modèle pré-entrainé
model = YOLO("yolo-Weights/yolov8n.pt")

# Lancer l'entraînement avec les nouvelles données
model.train(data="data.yaml", epochs=50, imgsz=640, batch=16, pretrained=True)
