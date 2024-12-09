# views.py
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommandSerializer
from .utils.Assistant import Assistant
from .utils.Chatbot import Chatbot
from .utils.SearchingFromWeb import SearchingFromWeb
from .utils.ControlAppWeb import ControlAppWeb 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
import json
class VoiceAssistantAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        # Deserialize the request data
        serializer = CommandSerializer(data=request.data)
        
        if serializer.is_valid():
            command = serializer.validated_data['command']
            assistant = Assistant()
            web_search = SearchingFromWeb(assistant)
            control_app_web = ControlAppWeb(assistant)
            chatbot = Chatbot()

            if "wake up" in command:
                return Response({"response": "Hello, How can I assist you?"})
            elif "change voice" in command:
                assistant.toggle_voice()
                return Response({"response": "Voice changed."})
            elif "google" in command:
                result = web_search.search_google(command)
                assistant.speak(result)
                return Response({"response": result})

            elif "youtube" in command:
                result = web_search.search_youtube(command)
                assistant.speak(result)
                return Response({"response": result})

            elif "open" in command:
                result = control_app_web.open_webapp(command)
                assistant.speak(result)
                return Response({"response": result})

            elif "chat" in command:
                response = chatbot.generate_response(command)
                assistant.speak(response)
                return Response({"response": response})

            elif "the time" in command:
                time = datetime.datetime.now().strftime("%H:%M")
                assistant.speak(f"Sir, the time is {time}")
                return Response({"response": time})

            return Response({"response": "No valid command recognized."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
