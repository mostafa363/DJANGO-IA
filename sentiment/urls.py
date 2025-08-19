from rest_framework import routers
from .views import SentimentAnalysisViewSet
from .views_html import sentiment_list
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'sentiments', SentimentAnalysisViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', sentiment_list, name='sentiment-list'),
]
