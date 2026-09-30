import os
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from src.data_loader import load_dataset
from src.preprocess import extract_features


def main():
    print("Loading dataset...")

    image_paths, labels = load_dataset()

    features = []
    valid_labels = []

    print("Extracting image features...")

    for i, image_path in enumerate(image_paths):
        try:
            feature = extract_features(image_path)
            features.append(feature)
            valid_labels.append(labels[i])
        except Exception as e:
            print("Skipped:", image_path, "|", e)

    X = np.array(features)
    y = np.array(valid_labels)

    print("Feature extraction complete.")
    print("Total valid images:", len(X))

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("Training SVM model...")

    model = SVC(
        kernel="rbf",
        probability=True,
        class_weight="balanced",
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("\nTraining completed!")
    print("Accuracy:", round(accuracy * 100, 2), "%")

    print("\nClassification Report:")
    print(classification_report(
        y_test,
        predictions,
        target_names=["Legitimate", "Phishing"]
    ))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    os.makedirs("models", exist_ok=True)

    model_path = "models/phishing_detector.joblib"
    joblib.dump(model, model_path)

    print("\nModel saved to:", model_path)


if __name__ == "__main__":
    main()