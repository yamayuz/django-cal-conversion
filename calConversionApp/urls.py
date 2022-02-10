from django.urls import path
from .views import ConvView, TestView

urlpatterns = [
    path('conv/', ConvView.as_view(), name='conv'),
]
