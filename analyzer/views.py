from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from textblob import TextBlob
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
            analysis = TextBlob(text)
            score = analysis.sentiment.polarity  # Correct TextBlob usage
            if score > 0.1:
                sentiment = "positive"
            elif score < -0.1:
                sentiment = "negative"
            else:
                sentiment = "neutral"
            SentimentAnalysis.objects.create(user=request.user, text=text, sentiment=sentiment, score=score)

    return render(request, "analyze.html", {"sentiment": sentiment, "score": score, "text": text, "error": error})
