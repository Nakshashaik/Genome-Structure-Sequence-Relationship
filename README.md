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

## 📂 Project Structure
