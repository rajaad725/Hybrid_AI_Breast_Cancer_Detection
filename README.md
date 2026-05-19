# Hybrid AI for Breast Cancer Detection Using Combined Clinical Features and Mammographic Imaging

## Overview

Breast cancer diagnosis is a critical healthcare challenge where early and accurate detection can significantly improve patient outcomes. This project presents a **Hybrid Artificial Intelligence system** that combines **clinical tabular data** and **mammographic imaging** to improve breast cancer classification performance.

The study evaluates three different AI approaches:

- **Baseline A:** Traditional Machine Learning using clinical features  
- **Baseline B:** Deep Learning using mammographic images  
- **Baseline C:** Multimodal Hybrid AI using late fusion of clinical + imaging data  

The goal is to investigate whether combining multiple data modalities improves diagnostic performance compared to single-modality systems.

---

## Problem Statement

Most existing breast cancer AI systems rely on either clinical data or imaging data. However, real-world diagnosis is inherently multimodal. This project addresses this limitation by building a hybrid multimodal AI framework.

---

## Research Objectives

- Develop machine learning models using clinical data  
- Develop deep learning models using mammographic images  
- Design a multimodal fusion model using late fusion  
- Compare performance across all baselines  
- Evaluate impact of class imbalance  
- Visualise results using ROC curves and confusion matrices  

---

## Dataset

The project uses the **TOMPEI-CMMD Dataset** from The Cancer Imaging Archive (TCIA).

Kashiwada, Y. et al. (2025). *TOMPEI-CMMD Dataset (Version 1)*.  
DOI: https://doi.org/10.7937/WEZW-BH22  

License: CC BY 4.0  

---

## Methodology

### Baseline A — Clinical Machine Learning
- Logistic Regression  
- Random Forest  
- SVM  

### Baseline B — Image-Based Deep Learning
- ResNet  
- EfficientNet  

### Baseline C — Multimodal AI
- Late fusion of clinical + image embeddings  
- Final classification layer  

---

## Technologies Used

- Python  
- PyTorch  
- Scikit-learn  
- Pandas  
- NumPy  
- OpenCV  
- Matplotlib  
- Seaborn  
- Google Colab  

---

---

## Model Performance

### Baseline A — Clinical ML

| Model | Accuracy |
|------|----------|
| Logistic Regression | 87.7% |
| Random Forest | 88.9% |
| SVM | 87.2% |

Best model: Random Forest

---

### Baseline B — Deep Learning

- ResNet: 85%  
- EfficientNet: 85%  

---

### Baseline C — Hybrid Model

- Accuracy: 85%  
- Improved minority-class recall  
- More robust than single models  

---

## Key Findings

- Clinical data alone performs strongly  
- CNN models struggle with imbalance  
- Multimodal fusion improves robustness  
- Class imbalance is a key challenge  

---
## Run notebooks in:

Google Colab

Jupyter Notebook

VS Code

## Author:

Raja Abdullah Shafique

BSc Computer Science with Artificial Intelligence

## Disclaimer:
This project is for academic purposes only and not intended for clinical use.

## Project Structure

```bash
Hybrid_AI_Breast_Cancer_Detection/
│
├── 01_Data_Raw/
│   ├── Images_Dataset/
│   ├── Tabular_Dataset/
│
├── 02_Data_Processed/
│   ├── CMMD_Aligned/
│   ├── Processed_Images/
│
├── 03_Notebooks/
│
├── 04_Report_Materials/
│
├── 05_Results/
│
├── LICENSE.txt
└── README.md

---
