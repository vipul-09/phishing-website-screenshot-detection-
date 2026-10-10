import cv2
import numpy as np

from src.preprocess import extract_features


def test_extract_features():
    image = np.zeros((160, 256, 3), dtype=np.uint8)

    cv2.imwrite("test_image.png", image)

    features = extract_features("test_image.png")

    assert features is not None
    assert len(features) > 0