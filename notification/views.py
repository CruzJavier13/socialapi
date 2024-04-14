from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class NotificationView(APIView):
    
    def get(self, request, pk=None, *args, **kwargs):
        return Response({"Message":"Notification"})
