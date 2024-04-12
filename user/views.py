from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUserAuth, User
from .serializer import UserSerializer
from rest_framework import status
#from django.shortcuts import render

# Create your views here.
class UserView(APIView):
    
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        print(args)
        print(kwargs)
        # Verifica si los datos son válidos según el serializer
        if user_serializer.is_valid():
            # Guarda los datos en la base de datos
            user_serializer.save()
            
            # Devuelve una respuesta con los datos guardados y un código de estado 201 (CREATED)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Si los datos no son válidos, devuelve una respuesta con los errores y un código de estado 400 (BAD REQUEST)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'not found'})
    
