from django.shortcuts import render
from textblob import TextBlob

from .models import SentimentAnalysis


# Create your views here.


def analyze_text(request):
    sentiment = None
    score = None
    text = ""

    if request.method == 'POST':
        text = request.POST.get('text', "")
        analysis = TextBlob(text)
        score = analysis.sentiment.polarity

        if score > 0:
            sentiment = "positive"

        elif score < 0:
            sentiment = "negative"

        else:
            sentiment = "neutral"

        SentimentAnalysis.objects.create(text=text, sentiment=sentiment, score=score)

    return render(request, "index.html", {"sentiment": sentiment, "score": score, "text": text})
    # return render(request, "analyzer/index.html", {"sentiment": sentiment, "score": score, "text": text})
