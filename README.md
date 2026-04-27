# 🧬 Deep Learning Approaches for Genome Structure–Sequence Relationship

## 📌 Overview
This project investigates whether **DNA sequence alone can predict chromatin interactions**, which are essential for gene regulation and 3D genome organization.

A **dual-branch Convolutional Neural Network (CNN)** is developed to model interactions between promoter and enhancer regions using only genomic sequence data, eliminating the need for expensive experimental techniques like Hi-C.

---

## 🧠 Problem Statement
Chromatin interactions regulate gene expression by bringing distant DNA regions into proximity.  
Traditional methods like Hi-C are:
- Expensive  
- Time-consuming  
- Not scalable across conditions  

👉 This project aims to **predict promoter–enhancer interactions using only DNA sequence information**.

---

## 🚀 Features
- 🧬 Sequence-based chromatin interaction prediction  
- 🧠 Dual-input CNN architecture  
- ⚖️ Distance-matched negative sampling  
- 🧪 Promoter-level data split (prevents data leakage)  
- 📊 Performance evaluation using ROC-AUC  

---

## 🏗️ Model Architecture
- Two input branches:
  - Promoter sequence  
  - Enhancer sequence  
- 1D Convolutional layers extract sequence motifs  
- Feature concatenation  
- Fully connected layers for classification  
- Sigmoid activation → interaction probability  

---

## 🧭 Description
- **data/** → Contains raw and processed genomic datasets  
- **notebooks/** → Jupyter notebooks for experiments and analysis  
- **src/** → Core source code (data processing, models, training)  
- **models/** → Saved trained models and checkpoints  
- **results/** → Performance metrics and visualizations  
- **app/** → Flask-based deployment (optional)  
- **main.py** → Runs the training pipeline  

---

## 🛠️ Tech Stack
- 🐍 Python  
- 🔥 PyTorch  
- 📊 NumPy, Pandas  
- 🧬 pyfaidx (genome sequence extraction)  
- 📈 scikit-learn (evaluation metrics)  
- 🌐 Flask (deployment)  

---

## 📊 Model Performance

| Model                     | Accuracy | AUC   | Insight |
|--------------------------|---------|-------|--------|
| Distance-Based Model      | ~0.55   | ~0.49 | Weak baseline |
| Feedforward NN (FNN)     | ~0.74   | ~0.82 | Limited learning |
| CNN                      | ~0.94   | ~0.98 | Strong performance |
| CNN (Promoter Split)     | ~0.78   | ~0.87 | Generalized model |

👉 CNN clearly outperforms other models by capturing sequence patterns.

---

## ⚙️ Installation

```bash
git clone https://github.com/NakshaShaik/Genome-Structure-Sequence-Relationship.git
cd Genome-Structure-Sequence-Relationship
pip install -r requirements.txt
