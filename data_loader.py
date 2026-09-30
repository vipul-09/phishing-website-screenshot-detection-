import os

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")


def get_image_paths():
    dataset_path = "dataset"

    legitimate_path = os.path.join(dataset_path, "legitimate")
    phishing_path = os.path.join(dataset_path, "phishing")

    images = []
    labels = []

    for filename in os.listdir(legitimate_path):
        if filename.lower().endswith(IMAGE_EXTENSIONS):
            images.append(os.path.join(legitimate_path, filename))
            labels.append(0)

    for filename in os.listdir(phishing_path):
        if filename.lower().endswith(IMAGE_EXTENSIONS):
            images.append(os.path.join(phishing_path, filename))
            labels.append(1)

    return images, labels


def load_dataset():
    return get_image_paths()