from transformers import pipeline

# Initialize sentiment-analysis pipeline
sentiment_analyzer = pipeline('sentiment-analysis')

def analyze_sentiment(user_input):
    # Analyze the sentiment of the user input
    sentiment = sentiment_analyzer(user_input)
    return sentiment[0]
