from django.urls import path
from .views import image_to_caption, chatbot

urlpatterns = [
    path('chatbot/', chatbot, name='chatbot'),
    path('image-caption/', image_to_caption, name='image_caption'),
]