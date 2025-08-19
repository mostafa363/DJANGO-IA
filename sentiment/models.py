from django.db import models

class SentimentAnalysis(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.author}: {self.sentiment}"
