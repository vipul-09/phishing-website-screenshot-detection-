# Project Statement

## Project Title

AI-Based Phishing Website Screenshot Detection Using Computer Vision

## Problem Statement

Phishing websites often imitate the visual appearance of legitimate websites to deceive users. This project aims to develop a computer-vision-based system that analyzes a website screenshot and classifies it as either legitimate or phishing.

## Scope

The project focuses on detecting phishing websites using visual information available in website screenshots. It uses image preprocessing, HOG feature extraction, and an SVM machine learning classifier.

The system does not analyze website URLs, HTML code, JavaScript, domain information, or live website behavior.

## Target Users

- Internet users
- Students and researchers studying phishing detection
- Cybersecurity learners
- Organizations interested in visual phishing detection

## High-Level Features

1. Website screenshot input
2. Image preprocessing
3. HOG-based visual feature extraction
4. SVM-based classification
5. Legitimate/phishing prediction
6. Prediction confidence
7. Model evaluation
8. Automated preprocessing testing

## Expected Input

A screenshot of a website in JPG, JPEG, PNG, BMP, or WEBP format.

## Expected Output

The system provides:

- Classification: Legitimate or Phishing
- Prediction confidence

## Technologies

- Python
- OpenCV
- NumPy
- Scikit-image
- Scikit-learn
- Joblib
- Pytest