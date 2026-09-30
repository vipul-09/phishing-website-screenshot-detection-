import cv2
import numpy as np
from skimage.feature import hog

IMAGE_SIZE = (256, 160)

def load_and_preprocess(image_path):
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    image = cv2.resize(image, IMAGE_SIZE)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = gray.astype("float32") / 255.0
    return gray

def extract_features(image_path):
    gray = load_and_preprocess(image_path)
    features = hog(
        gray,
        orientations=9,
        pixels_per_cell=(16, 16),
        cells_per_block=(2, 2),
        block_norm="L2-Hys"
    )
    return features
