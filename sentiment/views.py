from rest_framework import viewsets
from .models import SentimentAnalysis
from .serializers import SentimentAnalysisSerializer
from rest_framework.response import Response
from rest_framework import status

# Hugging Face sentiment analysis
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased")

class SentimentAnalysisViewSet(viewsets.ModelViewSet):
    queryset = SentimentAnalysis.objects.all()
    serializer_class = SentimentAnalysisSerializer

    def create(self, request, *args, **kwargs):
        text = request.data.get('text', '')
        author = request.data.get('author', '')
        # Analyse du sentiment
        result = sentiment_pipeline(text)[0]
        sentiment = result['label']
        data = {
            'text': text,
            'sentiment': sentiment,
            'author': author
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
