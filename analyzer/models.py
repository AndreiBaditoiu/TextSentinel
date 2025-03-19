from django.db import models


# Create your models here.

class SentimentAnalysis(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10)
    score = models.FloatField()
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}...-{self.sentiment} 9{self.score})"
