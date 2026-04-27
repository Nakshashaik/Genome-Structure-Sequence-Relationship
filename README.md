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

genome-ai/
│
├── data/
│   ├── raw/                     # Original dataset (xls, fasta)
│   ├── processed/               # Cleaned + encoded data
│   └── sample/                  # Small subset for testing
│
├── notebooks/
│   ├── EDA.ipynb               # Data exploration
│   ├── preprocessing.ipynb     # Sequence extraction & encoding
│   └── experiments.ipynb       # Model experiments
│
├── src/
│   ├── __init__.py
│   │
│   ├── data/
│   │   ├── loader.py           # Load dataset
│   │   ├── preprocess.py       # Cleaning + filtering
│   │   └── sequence.py         # DNA extraction (pyfaidx)
│   │
│   ├── features/
│   │   └── encoding.py         # One-hot encoding
│   │
│   ├── models/
│   │   ├── cnn_model.py        # Dual-branch CNN
│   │   ├── fnn_model.py        # Feedforward NN
│   │   └── baseline.py         # Distance model
│   │
│   ├── training/
│   │   ├── train.py            # Training loop
│   │   └── evaluate.py         # Metrics (ROC, AUC)
│   │
│   └── utils/
│       ├── config.py           # Hyperparameters
│       └── helpers.py          # Common functions
│
├── models/
│   ├── saved/                  # Trained models (.pth)
│   └── checkpoints/            # Intermediate saves
│
├── results/
│   ├── plots/                  # ROC curves, graphs
│   └── metrics/                # Accuracy, AUC logs
│
├── app/
│   ├── app.py                  # Flask backend
│   ├── templates/              # HTML files
│   └── static/                 # CSS (Tailwind)
│
├── requirements.txt
├── main.py                     # Entry point
├── README.md
└── .gitignore
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

👉 CNN clearly outperforms other models by capturing sequence patterns :contentReference[oaicite:0]{index=0}  

---

## ⚙️ Installation

```bash
git clone https://github.com/NakshaShaik/Genome-Structure-Sequence-Relationship.git
cd Genome-Structure-Sequence-Relationship
pip install -r requirements.txt

## 🔬 Methodology

- Extract DNA sequences (±2000 bp) from the hg19 reference genome  
- Convert sequences into numerical format using one-hot encoding  
- Train a dual-branch Convolutional Neural Network (CNN)  
- Generate distance-matched negative samples to balance the dataset  
- Evaluate model performance using ROC-AUC and accuracy metrics  
- Apply promoter-level data splitting to ensure unbiased testing and prevent data leakage  

---

## 📈 Results

- CNN achieves AUC up to **0.98**  
- Significantly outperforms traditional and baseline models  
- Demonstrates that DNA sequence contains meaningful interaction information  

---

## 🎯 Future Enhancements

- Transformer-based models (e.g., DNABERT)  
- Integration of multi-omics data  
- Model interpretability techniques (feature importance, attention maps)  
- Deployment as a web-based application  

---

## 👩‍💻 Authors

- P. Sugamya  
- Naksha Shaik  
- D. Nithyasri  

---

## 🏫 Institution

**G. Narayanamma Institute of Technology & Science (GNITS)**  
Affiliated to Jawaharlal Nehru Technological University Hyderabad (JNTUH)  
