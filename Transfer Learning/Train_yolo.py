from ultralytics import YOLO

# Charger le modèle pré-entrainé
model = YOLO("yolo-Weights/yolov8n.pt")

# Réinitialiser les classes pour correspondre à vos nouvelles classes
model.reset_head(num_classes=3)  # Vos nouvelles classes uniquement

# Lancer l'entraînement avec les nouvelles données
model.train(data="data.yaml", epochs=50, imgsz=640, batch=16)
