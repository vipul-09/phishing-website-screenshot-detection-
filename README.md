# AI-Based Phishing Website Screenshot Detection Using Computer Vision

## Project Overview

This project presents an AI-based computer vision system for detecting whether a website screenshot is **legitimate** or **phishing**.

The system processes website screenshots, extracts visual features using **Histogram of Oriented Gradients (HOG)**, and uses a **Support Vector Machine (SVM)** classifier to predict the class of the website.

The project is designed as a lightweight, CPU-friendly command-line application.

---

## Problem Statement

Phishing websites are designed to imitate legitimate websites and deceive users into entering sensitive information such as usernames, passwords and financial details.

Traditional URL-based detection methods may not always identify visually deceptive websites. This project explores a computer vision-based approach that analyzes the visual appearance of website screenshots to classify them as legitimate or phishing.

---

## Objectives

- Detect phishing websites using website screenshots.
- Apply image preprocessing techniques to standardize input images.
- Extract visual features using HOG.
- Train an SVM-based machine learning classifier.
- Evaluate the classification performance using standard metrics.
- Provide a simple command-line interface for prediction.

---

## Main Features

### 1. Image Preprocessing

- Loads website screenshots.
- Resizes images to a fixed size.
- Converts images to grayscale.
- Normalizes image values.

### 2. HOG Feature Extraction

- Extracts Histogram of Oriented Gradients features.
- Represents visual structures and edge information numerically.

### 3. SVM Classification

- Uses a Support Vector Machine with an RBF kernel.
- Uses balanced class weights to handle class imbalance.

### 4. Model Evaluation

- Calculates accuracy, precision, recall and F1-score.
- Generates a confusion matrix.

### 5. Command-Line Prediction

- Accepts a website screenshot as input.
- Predicts whether it is legitimate or phishing.
- Displays prediction confidence.

---

## Technologies Used

- Python
- OpenCV
- NumPy
- Scikit-image
- Scikit-learn
- Joblib
- Matplotlib
- Seaborn
- Pytest
- Git and GitHub

---

## Dataset

The project uses the **Phishing Sites Screenshot** dataset available on Kaggle.

Dataset source:

https://www.kaggle.com/datasets/zackyzac/phishing-sites-screenshot

The dataset contains screenshots belonging to two classes:

- `legitimate`
- `phishing`

### Dataset Distribution

| Class | Number of Images |
|---|---:|
| Legitimate | 1,147 |
| Phishing | 550 |
| Total | 1,697 |

The dataset is not included in this GitHub repository because of its large size.
### Dataset Setup

After downloading the dataset, organize the images in the following structure:

```text
dataset/
├── legitimate/
└── phishing/
```

---

## Project Workflow

```text
Website Screenshot
        ↓
Image Preprocessing
        ↓
Resize + Grayscale + Normalization
        ↓
HOG Feature Extraction
        ↓
SVM Classifier
        ↓
Prediction
        ↓
Legitimate / Phishing
        ↓
Confidence Score
```

---

## Project Structure

```text
Phishing-Website-Screenshot-Detection/
│
├── dataset/
│   ├── legitimate/
│   └── phishing/
│
├── models/
├── results/
│
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── data_loader.py
│   ├── train_model.py
│   ├── predict.py
│   ├── evaluate.py
│   └── utils.py
│
├── tests/
│   └── test_preprocess.py
│
├── main.py
├── requirements.txt
├── README.md
├── statement.md
├── PROJECT_REPORT_TEMPLATE.md
└── .gitignore
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Diviv07/phishing-website-screenshot-detection.git
cd phishing-website-screenshot-detection
```

### 2. Create a Virtual Environment

For Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

For Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training the Model

Make sure the dataset is organized as:

```text
dataset/
├── legitimate/
└── phishing/
```

Run the training module:

```bash
python -m src.train_model
```

The trained model will be saved as:

```text
models/phishing_detector.joblib
```

---

## Model Evaluation

Run the evaluation module:

```bash
python -m src.evaluate
```

The evaluation calculates:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The metrics are saved in:

```text
results/metrics.csv
```

---

## Making a Prediction

To classify a website screenshot, run:

```bash
python main.py --image "path/to/screenshot.png"
```

Example:

```bash
python main.py --image "Screenshot 2026-09-13 103407.png"
```

Example output:

```text
========================================
 AI-BASED PHISHING SCREENSHOT DETECTOR
========================================
Input      : Screenshot 2026-09-13 103407.png
Prediction : LEGITIMATE
Confidence : 76.96%
========================================
```

---

## Testing

The project includes a unit test for the image feature extraction module.

On Windows PowerShell:

```powershell
$env:PYTHONPATH="."
pytest
```

On Linux/macOS:

```bash
PYTHONPATH=. pytest
```

Example successful output:

```text
1 passed
```

---

## Experimental Results

The HOG + SVM model was evaluated using an 80:20 stratified train-test split.

| Metric | Value |
|---|---:|
| Accuracy | 67.65% |
| Precision | 50.00% |
| Recall | 67.27% |
| F1-score | 57.36% |

### Confusion Matrix

```text
                 Predicted
              Legitimate  Phishing

Actual
Legitimate        156        74
Phishing           36        74
```

The results demonstrate that the system can distinguish between legitimate and phishing website screenshots, while also showing that further improvement is possible.

---

## Functional Modules

### Preprocessing Module

Responsible for loading, resizing, converting and normalizing images and extracting HOG features.

### Data Loading Module

Responsible for reading image paths and assigning legitimate and phishing labels.

### Training Module

Responsible for preparing the dataset, training the SVM classifier and saving the trained model.

### Prediction Module

Responsible for processing a new screenshot and generating the classification result.

### Evaluation Module

Responsible for calculating performance metrics and generating evaluation results.

### Testing Module

Responsible for testing the preprocessing and feature extraction functionality.

---

## Non-Functional Requirements

### Performance

The system should perform prediction efficiently on a standard computer without requiring a GPU.

### Usability

The application provides a simple command-line interface for screenshot classification.

### Maintainability

The source code is separated into multiple modules to improve readability and maintainability.

### Reliability

The system validates image input and handles invalid or unsupported image files.

### Portability

The project uses Python and commonly available machine learning libraries and can run on different operating systems with the required dependencies installed.

---

## Limitations

- The model uses screenshot-based visual information only.
- It does not analyze URLs, HTML source code or website network behavior.
- The dataset contains fewer phishing images than legitimate images.
- The current HOG + SVM approach has moderate classification performance.
- A screenshot alone may not contain enough information to identify every type of phishing website.
- The confidence score should not be treated as a guarantee that a website is safe.

---

## Future Enhancements

1. Use a larger and more diverse screenshot dataset.
2. Improve class balance between legitimate and phishing samples.
3. Experiment with CNN and transfer learning models.
4. Combine screenshot-based features with URL and HTML-based features.
5. Add data augmentation techniques.
6. Improve model performance through hyperparameter tuning.
7. Develop a web-based interface for easier usage.
8. Add explainable AI techniques to show why a screenshot was classified as phishing.
9. Evaluate the system on unseen real-world websites.
10. Compare HOG + SVM with deep learning approaches.

---

## GitHub and Version Control

The project is maintained using Git and GitHub.

Repository:

https://github.com/vipul-09/phishing-website-screenshot-detection

Large dataset files and generated model files are excluded from version control using `.gitignore`.

---

## Project Statement

A separate project statement is provided in:

```text
statement.md
```

It includes:

- Problem Statement
- Project Scope
- Target Users
- High-Level Features
- Expected Input and Output
- Technologies Used

---

## Command Summary

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python -m src.train_model
```

### Evaluate Model

```bash
python -m src.evaluate
```

### Predict a Screenshot

```bash
python main.py --image "path/to/screenshot.png"
```

### Run Tests

```powershell
$env:PYTHONPATH="."
pytest
```

---

## Conclusion

This project demonstrates a computer vision-based approach for identifying phishing websites from screenshots.

By combining image preprocessing, HOG feature extraction and an SVM classifier, the system provides a lightweight command-line solution for classifying website screenshots as legitimate or phishing.

The project also demonstrates the practical application of computer vision, machine learning, modular software design, testing and Git-based version control.

---

## References

1. Phishing Sites Screenshot Dataset, Kaggle.  
   https://www.kaggle.com/datasets/zackyzac/phishing-sites-screenshot

2. Scikit-image Documentation.  
   https://scikit-image.org/docs/

3. Scikit-learn Documentation.  
   https://scikit-learn.org/

4. OpenCV Documentation.  
   https://docs.opencv.org/

5. Pytest Documentation.  
   https://docs.pytest.org/

---

## Disclaimer

This project is developed for academic and educational purposes as part of a Computer Vision course evaluation.

The system is a research and learning prototype and should not be considered a replacement for professional cybersecurity tools or security analysis systems.
