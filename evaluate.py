import os
import csv
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from src.data_loader import load_dataset
from src.preprocess import extract_features


def main():
    print("Loading dataset...")

    image_paths, labels = load_dataset()

    features = []
    valid_labels = []

    print("Extracting features...")

    for i, image_path in enumerate(image_paths):
        try:
            feature = extract_features(image_path)
            features.append(feature)
            valid_labels.append(labels[i])
        except Exception as e:
            print("Skipped:", image_path, "|", e)

    X = np.array(features)
    y = np.array(valid_labels)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    import joblib

    model = joblib.load("models/phishing_detector.joblib")

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    matrix = confusion_matrix(y_test, predictions)

    print("\nEvaluation Results")
    print("------------------")
    print("Accuracy:", round(accuracy * 100, 2), "%")
    print("Precision:", round(precision, 4))
    print("Recall:", round(recall, 4))
    print("F1 Score:", round(f1, 4))

    print("\nConfusion Matrix:")
    print(matrix)

    os.makedirs("results", exist_ok=True)

    with open("results/metrics.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Metric", "Value"])
        writer.writerow(["Accuracy", accuracy])
        writer.writerow(["Precision", precision])
        writer.writerow(["Recall", recall])
        writer.writerow(["F1 Score", f1])

    print("\nResults saved to: results/metrics.csv")


if __name__ == "__main__":
    main()
    