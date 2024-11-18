import os

# Dossier contenant les fichiers labels
labels_dir = "train/labels"  # Changez par le chemin vers vos labels (train/labels, valid/labels, etc.)

# Correspondance entre anciennes classes et nouvelles indices
class_mapping = {
    80: 0,  # Ancien indice pour "can" -> Nouvel indice
    81: 1,  # Ancien indice pour "snackbag" -> Nouvel indice
    82: 2   # Ancien indice pour "waterbottle" -> Nouvel indice
}

# Parcourir tous les fichiers labels dans le dossier
for label_file in os.listdir(labels_dir):
    if label_file.endswith(".txt"):
        file_path = os.path.join(labels_dir, label_file)

        # Lire et corriger les annotations
        with open(file_path, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            class_id = int(parts[0])

            # Si la classe doit être remappée
            if class_id in class_mapping:
                parts[0] = str(class_mapping[class_id])  # Remplacer par le nouvel indice
                new_lines.append(" ".join(parts))

        # Écrire les annotations corrigées dans le fichier
        with open(file_path, "w") as f:
            f.write("\n".join(new_lines))