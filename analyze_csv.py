import pandas as pd
from scripts.bias_scorer import analyze_job_description

def analyze_csv(filepath):
    df = pd.read_csv(filepath)
    for _, row in df.iterrows():
        print(f"Job Title: {row['job_title']} @ {row['company']}")
        analyze_job_description(row['description'])
        print()

if __name__ == "__main__":
    analyze_csv("data/sample_job_descriptions.csv")
