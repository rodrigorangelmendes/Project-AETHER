# Project AETHER

![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**Project AETHER** is a lightweight bias analysis tool for job descriptions.

---

## 🔹 Features

- Detects biased terms (e.g., "rockstar", "ninja", "warrior") in job descriptions.
- Calculates a **bias score** based on predefined weights.
- Supports analyzing multiple descriptions directly from a **CSV file**.
- Easy-to-use Python implementation.

---

## 🔹 Project Structure

Project-AETHER/
│
├── scripts/ # Main scripts
│ └── bias_scorer.py
├── data/ # Example datasets
│ └── sample_job_descriptions.csv
├── notebooks/ # Jupyter notebooks (optional)
├── guidelines/ # Documentation / guidelines
├── test.py # Basic tests
├── analyze_csv.py # CSV analysis script
├── setup.bat # Dependency installation (Windows)
├── README.md
├── LICENSE
└── .gitignore

---

## 🔹 Installation

1. Clone the repository:
git clone https://github.com/rodrigorangelmendes/Project-AETHER.git
cd Project-AETHER

2. Install dependencies (Windows):
.\setup.bat

Or manually:
pip install pandas matplotlib nltk
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

---

## 🔹 Usage

### Analyze a single job description
python scripts/bias_scorer.py

### Run tests
python test.py

### Analyze all descriptions from a CSV
python analyze_csv.py
