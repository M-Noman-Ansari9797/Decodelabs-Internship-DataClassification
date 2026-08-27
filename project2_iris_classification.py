"""
==========================================================
DecodeLabs — Project 2: Data Classification Using AI
==========================================================
Goal   : Build a basic classification model using a small dataset (Iris)
Skills : Data handling, supervised learning basics, model training
Pipeline (IPO Framework):
    INPUT   -> Iris dataset, feature scaling
    PROCESS -> Train-test split, KNN algorithm
    OUTPUT  -> Confusion Matrix, F1 Score
==========================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    f1_score,
    accuracy_score,
)

# ----------------------------------------------------------
# STEP 1: LOAD AND UNDERSTAND THE DATASET
# ----------------------------------------------------------
iris = load_iris()
X = iris.data                      # shape (150, 4) -> sepal/petal length & width
y = iris.target                    # shape (150,)   -> 0=Setosa, 1=Versicolor, 2=Virginica
feature_names = iris.feature_names
target_names = iris.target_names

df = pd.DataFrame(X, columns=feature_names)
df["species"] = pd.Categorical.from_codes(y, target_names)

print("=" * 60)
print("STEP 1: DATASET OVERVIEW")
print("=" * 60)
print(f"Samples : {df.shape[0]}")
print(f"Features: {len(feature_names)} -> {feature_names}")
print(f"Classes : {len(target_names)} -> {list(target_names)}")
print("\nClass balance:")
print(df["species"].value_counts())
print("\nFirst 5 rows:")
print(df.head())

# ----------------------------------------------------------
# STEP 2: TRAIN-TEST SPLIT (shuffle first to remove order bias)
# ----------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 80% train / 20% test
    random_state=42,    # reproducibility
    shuffle=True,
    stratify=y          # keep class balance equal in both sets
)

print("\n" + "=" * 60)
print("STEP 2: TRAIN-TEST SPLIT")
print("=" * 60)
print(f"Training samples: {X_train.shape[0]}")
print(f"Testing samples : {X_test.shape[0]}")

# ----------------------------------------------------------
# STEP 3: FEATURE SCALING (the "Gatekeeper Rule")
# Fit scaler ONLY on training data, then apply to both sets
# (prevents test-set information leaking into training)
# ----------------------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n" + "=" * 60)
print("STEP 3: FEATURE SCALING")
print("=" * 60)
print("Mean after scaling (train):", np.round(X_train_scaled.mean(axis=0), 2))
print("Std  after scaling (train):", np.round(X_train_scaled.std(axis=0), 2))

# ----------------------------------------------------------
# STEP 4: TUNE K (find the "elbow" - lowest error rate)
# ----------------------------------------------------------
error_rates = []
k_values = range(1, 21)

for k in k_values:
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    knn_temp.fit(X_train_scaled, y_train)
    pred_temp = knn_temp.predict(X_test_scaled)
    error_rates.append(np.mean(pred_temp != y_test))

best_k = k_values[np.argmin(error_rates)]

plt.figure(figsize=(8, 5))
plt.plot(k_values, error_rates, marker="o", linestyle="--", color="steelblue")
plt.axvline(best_k, color="orange", linestyle=":", label=f"Best K = {best_k}")
plt.title("Tuning the Engine: Choosing K")
plt.xlabel("K Value")
plt.ylabel("Error Rate")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("k_tuning_plot.png", dpi=150)
plt.show()
plt.close()

print("\n" + "=" * 60)
print("STEP 4: CHOOSING OPTIMAL K")
print("=" * 60)
print(f"Best K found: {best_k} (lowest error rate = {min(error_rates):.4f})")

# ----------------------------------------------------------
# STEP 5: TRAIN THE MODEL (Instantiate -> Fit -> Predict)
# ----------------------------------------------------------
model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(X_train_scaled, y_train)                 # FIT: memorize the map
predictions = model.predict(X_test_scaled)          # PREDICT: apply logic

print("\n" + "=" * 60)
print("STEP 5: MODEL TRAINING (KNN)")
print("=" * 60)
print(f"Model: KNeighborsClassifier(n_neighbors={best_k})")
print("Model trained and predictions generated on test set.")

# ----------------------------------------------------------
# STEP 6: OUTPUT VALIDATION — Confusion Matrix + F1 Score
# (Accuracy alone can be an "accuracy mirage" on imbalanced data)
# ----------------------------------------------------------
acc = accuracy_score(y_test, predictions)
f1_macro = f1_score(y_test, predictions, average="macro")
f1_weighted = f1_score(y_test, predictions, average="weighted")
cm = confusion_matrix(y_test, predictions)

print("\n" + "=" * 60)
print("STEP 6: OUTPUT VALIDATION")
print("=" * 60)
print(f"Accuracy      : {acc:.4f}")
print(f"F1 Score (macro)   : {f1_macro:.4f}")
print(f"F1 Score (weighted): {f1_weighted:.4f}")
print("\nConfusion Matrix:")
print(cm)
print("\nFull Classification Report:")
print(classification_report(y_test, predictions, target_names=target_names))

# Save confusion matrix plot
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
fig, ax = plt.subplots(figsize=(6, 6))
disp.plot(ax=ax, cmap="Blues", colorbar=False)
plt.title(f"Confusion Matrix (KNN, K={best_k})")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=150)
plt.show()
plt.close()

print("\n" + "=" * 60)
print("PROJECT 2 COMPLETE ✅")
print("=" * 60)
print("Saved: k_tuning_plot.png, confusion_matrix.png")
