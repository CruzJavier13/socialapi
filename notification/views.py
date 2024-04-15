from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .serialize import NotificationSerializer
from .models import Notification

class NotificationView:
    
    def get(self, request, *args, **kwargs):
        queriset = Notification.objects.all().exclude(is_view=False)
        notification_serializer = NotificationSerializer(queriset, many=True)

        return Response(notification_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        notification_serializer = NotificationSerializer(request.data)
        if notification_serializer.is_valid():
            notification_serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(notification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):
        instance = get_object_or_404(Notification, pk)
        notification_Serializer = NotificationSerializer(instance, data=request.data)
        if notification_Serializer.is_valid():
            notification_Serializer.save()
            return Response(notification_Serializer.data, status=status.HTTP_200_OK)
        return Response(notification_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            instance = get_object_or_404(Notification, pk=pk)
            serializer = NotificationSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(request.data, status=status.HTTP_200_OK)
            
