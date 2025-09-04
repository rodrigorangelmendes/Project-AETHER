@echo off
echo Installing required packages...
pip install pandas matplotlib nltk
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
echo Setup complete!
