from scripts.bias_scorer import analyze_job_description

test_texts = [
    "We need a rockstar ninja developer",
    "Looking for collaborative team player",
    "Seeking competitive warrior"
]

for text in test_texts:
    print(f"Testing: {text}")
    analyze_job_description(text)
    print()
