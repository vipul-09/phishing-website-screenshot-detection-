import argparse
from pathlib import Path
from src.predict import predict

def main():
    parser = argparse.ArgumentParser(
        description="AI-Based Phishing Website Screenshot Detection"
    )
    parser.add_argument(
        "--image",
        required=True,
        help="Path to a website screenshot"
    )
    parser.add_argument(
        "--model",
        default="models/phishing_detector.joblib",
        help="Path to trained model"
    )

    args = parser.parse_args()

    if not Path(args.image).exists():
        raise FileNotFoundError(f"Image not found: {args.image}")

    if not Path(args.model).exists():
        raise FileNotFoundError(
            "Trained model not found. Run: python -m src.train_model"
        )

    label, confidence = predict(args.image, args.model)

    print("\n========================================")
    print(" AI-BASED PHISHING SCREENSHOT DETECTOR")
    print("========================================")
    print(f"Input      : {args.image}")
    print(f"Prediction : {label}")
    print(f"Confidence : {confidence * 100:.2f}%")
    print("========================================\n")

if __name__ == "__main__":
    main()
