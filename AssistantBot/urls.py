from django.urls import path
from .views import VoiceAssistantAPIView

urlpatterns = [
    path('voice_assistant/', VoiceAssistantAPIView.as_view(), name='voice_assistant'),
]
