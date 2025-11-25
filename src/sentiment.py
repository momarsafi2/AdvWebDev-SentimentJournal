from typing import Tuple
from nltk.sentiment import SentimentIntensityAnalyzer

# Create the analyzer locally using VADER
_sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str) -> Tuple[float, str]:

    scores = _sia.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        label = "POSITIVE"
    elif compound <= -0.05:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"

    return compound, label
