# AETHER: Bias-Mitigation Analysis for IT Job Descriptions

## Overview
This self-directed research project explores linguistic bias in IT job descriptions using Natural Language Processing (NLP) techniques. The goal is to provide a data-driven framework and practical tools for creating more inclusive hiring materials.

## Motivation
As an IT recruitment professional, I've observed how language can unintentionally influence the diversity of applicant pools. This project aims to quantify that impact and offer actionable solutions.

## Features
- **Text Analysis:** Uses a rule-based system to detect potentially biased language (e.g., gendered terms, excessive jargon).
- **Bias Scoring:** Assigns an inclusivity score to job descriptions.
- **Suggestions:** Provides alternative, neutral wording for flagged terms.

## Methodology
1. **Data Collection:** Over 4,000 IT job descriptions were gathered from public sources.
2. **Analysis:** Conducted in a Jupyter Notebook using Python, Pandas, and Matplotlib.
3. **Rule-Based Scoring:** Developed a heuristic model based on known bias lexicons and linguistic patterns.
4. **Validation:** Findings were reviewed against established research on bias in hiring.

## Tools Used
- **Python** (Pandas, Matplotlib, NLTK)
- **Jupyter Notebook** & **Anaconda**
- **GitHub** for version control
- **ChatGPT/GPT-4** for research and conceptual guidance

## How to Use
1. **Clone the repository:**
   ```bash
   git clone https://github.com/rodrigorangelmendes/Project-AETHER.git
   cd Project-AETHER 
2. **Install dependencies:**
   ```bash
   pip install pandas matplotlib nltk jupyter
3. **Run the analysis notebook:**
   ```bash
   jupyter notebook notebooks/01_bias_analysis.ipynb
4. **Or use the standalone scorer:**
   ```bash
   python scripts/bias_scorer.py --text "Your job description text here"
