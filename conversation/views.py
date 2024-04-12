from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .serializer import ConversationSerializer
from .models import Conversation

# Create your views here.
class ConversationView(APIView):

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            try:
                conversation = Conversation.objects.get(pk=pk)
                serializer = ConversationSerializer(conversation)
                return Response(serializer.data)
            except Conversation.DoesNotExist:
                raise Http404
        else:
            queryset = Conversation.objects.all()
            serializer = ConversationSerializer(queryset, many=True)
            return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)