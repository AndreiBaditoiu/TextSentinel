from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from textblob import TextBlob

from .models import SentimentAnalysis


# Create your views here.

@login_required
def analyze_text(request):
    sentiment = None
    score = None
    text = ""

    if request.method == 'POST':
        text = request.POST.get('text', "")
        analysis = TextBlob(text)
        # analyzer = SentimentIntensityAnalyzer()
        score = analysis.sentiment.polarity


        if score > 0.1:
            sentiment = "positive"

        elif score < - 0.1:
            sentiment = "negative"

        else:
            sentiment = "neutral"

        SentimentAnalysis.objects.create(user=request.user, text=text, sentiment=sentiment, score=score)

        return render(request, "analyze.html", {"sentiment": sentiment, "score": score, "text": text})
    return render(request, "analyze.html")


@login_required
def analysis_history(request):
    analyses = SentimentAnalysis.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "history.html", {"analyses": analyses})