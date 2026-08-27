# Project 2 — Data Classification Using AI (Iris Dataset)

DecodeLabs Industrial Training Kit — AI Internship, Project 2.

A supervised learning pipeline that classifies iris flowers into three species
(Setosa, Versicolor, Virginica) using the K-Nearest Neighbors (KNN) algorithm.

## Overview

| Stage | Details |
|---|---|
| **Input** | Iris dataset (150 samples, 4 features, 3 classes) |
| **Process** | Feature scaling -> Train/Test split -> KNN classification |
| **Output** | Confusion Matrix, F1 Score, Accuracy |

## Pipeline

1. Load and explore the Iris dataset
2. Scale features with StandardScaler
3. Split data 80/20 (shuffled, stratified)
4. Tune K by sweeping K = 1 to 20 and picking the lowest error rate
5. Train a KNeighborsClassifier
6. Evaluate using a confusion matrix and F1 score (not accuracy alone)

## Results

- Accuracy: ~96.7%
- F1 Score (macro): ~0.967
- Only 1 misclassification out of 30 test samples

## Setup

pip install -r requirements.txt
python project2_iris_classification.py

Running the script generates two plots in the project folder:
- k_tuning_plot.png - error rate vs. K value
- confusion_matrix.png - model's confusion matrix on the test set

## Tech Stack

- Python
- scikit-learn
- pandas / numpy
- matplotlib

## Note

The K-value sweep picked K=1 for this dataset, which works well here since
Iris is small and cleanly separated, but K=1 is generally more sensitive to
noise than a slightly higher K (e.g. 5-7) on larger or noisier datasets.
