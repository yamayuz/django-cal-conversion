from django.urls import path
from .views import ConvView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('conv/', ConvView.as_view(), name='conv'),
] 
