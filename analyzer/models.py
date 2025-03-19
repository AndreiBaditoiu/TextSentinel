from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class SentimentAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    sentiment = models.CharField(max_length=10)
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}...-{self.sentiment} )"
