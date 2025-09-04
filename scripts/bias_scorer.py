import re
import sys

class SimpleBiasAnalyzer:
    def __init__(self):
        self.biased_terms = {
            'aggressive': {'category': 'masculine-coded', 'weight': 1.0, 'suggestion': 'determined'},
            'ninja': {'category': 'informal-jargon', 'weight': 0.8, 'suggestion': 'expert'},
            'rockstar': {'category': 'informal-jargon', 'weight': 0.8, 'suggestion': 'skilled professional'},
            'competitive': {'category': 'masculine-coded', 'weight': 0.7, 'suggestion': 'driven'},
            'warrior': {'category': 'masculine-coded', 'weight': 0.7, 'suggestion': 'dedicated professional'}
        }
        
        self.stop_words = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to'}

    def calculate_bias_score(self, text):
        words = self._clean_and_tokenize(text)
        score = 0
        flagged_terms = []
        
        for word in words:
            if word in self.biased_terms:
                term_info = self.biased_terms[word]
                score += term_info['weight']
                flagged_terms.append(f"{word} ({term_info['category']})")
        
        return score, flagged_terms

    def _clean_and_tokenize(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        words = text.split()
        return [word for word in words if word not in self.stop_words and len(word) > 2]

def analyze_job_description(text):
    analyzer = SimpleBiasAnalyzer()
    score, flagged_terms = analyzer.calculate_bias_score(text)
    
    print("Bias Analysis Report")
    print("=" * 50)
    print(f"Score: {score}/10")
    print(f"Flagged terms: {', '.join(flagged_terms) if flagged_terms else 'None'}")
    print("=" * 50)

if __name__ == "__main__":
    text = "We need a rockstar ninja developer who can aggressively crush code"
    analyze_job_description(text)
