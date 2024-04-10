from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUserAuth, User
from .serializer import UserSerializer
#from django.shortcuts import render

# Create your views here.
class UserView(APIView):
    
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        return Response({'error':'not found'})
