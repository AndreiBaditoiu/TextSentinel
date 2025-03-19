from django.urls import path

from .views import analyze_text

urlpatterns = [
    path('', analyze_text, name='analyze_text'),
]
