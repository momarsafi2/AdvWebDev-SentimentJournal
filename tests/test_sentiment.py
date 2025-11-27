from src.sentiment import analyze_sentiment


def test_sentiment_positive():
    score, label = analyze_sentiment("I am very happy today!")
    assert score > 0
    assert label == "POSITIVE"

def test_sentiment_negative():
    score, label = analyze_sentiment("This is awful and terrible.")
    assert score < 0
    assert label == "NEGATIVE"

def test_sentiment_neutral():
    score, label = analyze_sentiment("The book is on the table.")
    assert label == "NEUTRAL"
