# AssistantBot/serializers.py
from rest_framework import serializers

class CommandSerializer(serializers.Serializer):
    command = serializers.CharField(max_length=255)