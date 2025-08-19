from django.shortcuts import render
from .models import SentimentAnalysis

def sentiment_list(request):
    sentiments = SentimentAnalysis.objects.all().order_by('-created_at')
    return render(request, 'sentiment/list.html', {'sentiments': sentiments})
