# PROJECT REPORT

## AI-Based Phishing Website Screenshot Detection Using Computer Vision

### 1. Cover Page

**Project Title:** AI-Based Phishing Website Screenshot Detection Using Computer Vision

**Course:** Computer Vision

**Student Name:** Vipul Kumar Verma

**Program:** B.Tech Computer Science and Engineering (AI/ML)

**Academic Year:** 2026

---

## 2. Introduction

Phishing attacks use deceptive websites to imitate legitimate online services. Visual similarity between a phishing page and a legitimate page can make manual identification difficult.

This project investigates whether visual information from website screenshots can be used to classify webpages as phishing or legitimate.

---

## 3. Problem Statement

Develop a computer-vision-based system that accepts a webpage screenshot and predicts whether it belongs to a phishing or legitimate website.

---

## 4. Objectives

1. Build a screenshot preprocessing pipeline.
2. Extract meaningful visual features.
3. Train a machine-learning classifier.
4. Evaluate classification performance.
5. Provide a simple command-line prediction interface.
6. Organize the solution into modular components.

---

## 5. Functional Requirements

### FR1 - Image Input
The system shall accept a website screenshot.

### FR2 - Image Preprocessing
The system shall resize and convert the image into a suitable representation.

### FR3 - Feature Extraction
The system shall extract visual features using HOG.

### FR4 - Classification
The system shall classify the screenshot as phishing or legitimate.

### FR5 - Evaluation
The system shall calculate accuracy, precision, recall and F1-score.

### FR6 - Command-Line Execution
The system shall allow predictions from a terminal.

---

## 6. Non-Functional Requirements

### Performance
The model should provide lightweight CPU-based inference.

### Usability
The system should be executable with simple terminal commands.

### Reliability
Invalid image paths and missing model files should be detected.

### Maintainability
Major processing stages should be separated into modules.

### Resource Efficiency
The project should avoid requiring a dedicated GPU.

---

## 7. System Architecture

```text
+----------------------+
| Website Screenshot   |
+----------+-----------+
           |
           v
+----------------------+
| Image Preprocessing  |
+----------+-----------+
           |
           v
+----------------------+
| HOG Feature          |
| Extraction           |
+----------+-----------+
           |
           v
+----------------------+
| SVM Classifier       |
+----------+-----------+
           |
           v
+----------------------+
| Phishing /           |
| Legitimate           |
+----------+-----------+
           |
           v
+----------------------+
| Confidence + Result  |
+----------------------+
```

---

## 8. Workflow Diagram

```text
Start
  |
  v
Load Screenshot
  |
  v
Validate Image
  |
  v
Resize + Grayscale
  |
  v
Extract HOG Features
  |
  v
Load Trained SVM
  |
  v
Predict Class
  |
  v
Calculate Confidence
  |
  v
Display Result
  |
  v
End
```

---

## 9. Use Case Diagram

```text
             +-----------------------------+
             | Phishing Screenshot System  |
             |                             |
Student ---> | Upload/Select Screenshot    |
Student ---> | Train Model                 |
Student ---> | Evaluate Model              |
Student ---> | Predict Screenshot          |
Student ---> | View Result                 |
             +-----------------------------+
```

---

## 10. Sequence Diagram

```text
User -> CLI: Provide screenshot path
CLI -> Preprocessor: Load image
Preprocessor -> Feature Extractor: Generate HOG features
Feature Extractor -> Classifier: Send feature vector
Classifier -> CLI: Prediction + probability
CLI -> User: Display result
```

---

## 11. Component/Class Structure

```text
data_loader.py
     |
     v
preprocess.py
     |
     v
train_model.py ----> phishing_detector.joblib
     |
     v
predict.py
     |
     v
main.py

evaluate.py ----> metrics.csv
tests/ ----------> validation
```

---

## 12. Dataset Description

The project uses the Kaggle "Phishing sites screenshot" dataset. The dataset provides screenshots of phishing and genuine websites organized into two categories.

Dataset source:

https://www.kaggle.com/datasets/zackyzac/phishing-sites-screenshot

The screenshots are used as visual input for the computer-vision pipeline.

---

## 13. Model Selection and Rationale

Histogram of Oriented Gradients (HOG) was selected because it represents local edge and shape information in images and is computationally lightweight.

Support Vector Machine (SVM) was selected as the classifier because it performs well on high-dimensional feature vectors and can run efficiently on a CPU.

This combination was selected to create a reproducible and resource-efficient Computer Vision baseline.

---

## 14. Implementation Details

The implementation is divided into separate modules:

- data_loader.py
- preprocess.py
- train_model.py
- predict.py
- evaluate.py
- utils.py
- main.py
- test_preprocess.py

The preprocessing stage resizes screenshots and converts them to grayscale. HOG features are then extracted and supplied to an SVM classifier.

---

## 15. Results

**IMPORTANT: Replace this section only after running the project. Do not invent values.**

Dataset samples used:

- Legitimate: ______
- Phishing: ______
- Total: ______

Evaluation:

- Accuracy: ______
- Precision: ______
- Recall: ______
- F1-score: ______

Confusion matrix:

[Insert generated confusion matrix here]

---

## 16. Screenshots

Insert screenshots of:

1. Project folder
2. Training command
3. Training output
4. Evaluation metrics
5. Prediction command
6. Prediction result

---

## 17. Testing Approach

The project includes an automated test for the image feature-extraction pipeline.

Command:

```bash
pytest
```

Additional validation includes:

- Checking whether the input image exists.
- Checking whether the image can be read.
- Checking whether both classes exist before training.
- Checking whether the trained model exists before prediction.

---

## 18. Challenges Faced

- Preparing screenshot data in a consistent folder structure.
- Converting website screenshots into useful visual features.
- Selecting a model that can run efficiently without requiring a GPU.
- Designing the project as multiple independent modules.
- Ensuring that the complete project can be executed through the command line.

---

## 19. Learnings and Key Takeaways

The project demonstrates the application of Computer Vision to a cybersecurity problem. It provides practical understanding of image preprocessing, feature extraction, supervised classification, model evaluation and modular Python development.

---

## 20. Future Enhancements

Future versions can use CNNs or Vision Transformers, combine screenshot features with URL/HTML features, provide explainability, and evaluate performance on larger cross-domain datasets.

---

## 21. References

1. ZACKY_ZAC, "Phishing sites screenshot," Kaggle.
2. Dalal, N. and Triggs, B., "Histograms of Oriented Gradients for Human Detection," CVPR, 2005.
3. Cortes, C. and Vapnik, V., "Support-vector networks," Machine Learning, 1995.
