import torch
from transformers import pipeline

device = 0 if torch.cuda.is_available() else -1

model_name = "distilbert-base-uncased-finetuned-sst-2-english"

sentiment_pipeline = pipeline(
    "sentiment-analysis", model=model_name, device=device)


def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result['label']
    score = result['score']

    if label == 'POSITIVE':
        sentiment = 'positive'
    elif label == 'NEGATIVE':
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    signed_score = score if sentiment == 'positive' else -score

    return label, score
