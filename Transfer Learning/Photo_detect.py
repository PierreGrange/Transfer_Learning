from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Charger le modèle YOLO entraîné
model_path = "runs/detect/train/weights/last.pt"  # Remplacez par le chemin de votre modèle
model = YOLO(model_path)

# Chemin vers l'image de test
image_path = "young-man-holding-can-cold-260nw-2459678745.jpg"  # Remplacez par le chemin de votre image


# Effectuer la prédiction
results = model(image_path)  # Cela retourne une liste de résultats

# Imprimer les informations sur les détections pour le premier résultat
for result in results:  # Parcours des résultats
    print(result)  # Résumé des prédictions
    print(result.boxes)  # Coordonnées des boîtes détectées
    print(result.probs)  # Probabilités associées aux classes (si disponible)

# Dessiner les résultats sur l'image
annotated_image = results[0].plot()  # Annoter l'image avec les détections

# Afficher l'image annotée
plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
