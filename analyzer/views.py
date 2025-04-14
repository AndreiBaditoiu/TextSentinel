from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .ml.sentiment_model import analyze_sentiment
from .models import SentimentAnalysis


@login_required
def analyze_text(request):
    sentiment = None
    score = None
    text = ""
    error = None

    if request.method == 'POST':
        text = request.POST.get('text', "").strip()
        if not text:
            error = "Text input cannot be empty."
        else:
            sentiment, score = analyze_sentiment(text)
            SentimentAnalysis.objects.create(user=request.user, text=text, sentiment=sentiment, score=score)

    return render(request, "analyze.html", {"sentiment": sentiment, "score": score, "text": text,
                                            "error": error})
