import joblib
from src.preprocess import extract_features

LABELS = {
    0: "LEGITIMATE",
    1: "PHISHING"
}

def predict(image_path, model_path="models/phishing_detector.joblib"):
    model = joblib.load(model_path)
    features = extract_features(image_path).reshape(1, -1)

    prediction = int(model.predict(features)[0])
    probabilities = model.predict_proba(features)[0]
    confidence = float(max(probabilities))

    return LABELS[prediction], confidence

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Detect phishing from a website screenshot.")
    parser.add_argument("--image", required=True, help="Path to website screenshot")
    args = parser.parse_args()

    label, confidence = predict(args.image)

    print("\n====================================")
    print(" PHISHING WEBSITE SCREENSHOT DETECTOR")
    print("====================================")
    print(f"Image      : {args.image}")
    print(f"Prediction : {label}")
    print(f"Confidence : {confidence * 100:.2f}%")
