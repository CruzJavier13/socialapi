from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CommentSerializer, LikeCommentSerializer, LikePostSerializer
from rest_framework import status
from django.http import Http404
from .models import CommentPost, LikeComment, LikePost

# Create your views here.
class CommentView(APIView):
    
    def get(self,request, pk=None, *args, **kwargs):
        if pk is not None:
            try:
                queryset = CommentPost.objects.get(pk=pk)
                comment_serializer = CommentSerializer(queryset)
            except CommentPost.DoesNotExist:
                raise Http404
        else:
            queryset = CommentPost.objects.all()
            comment_serializer = CommentSerializer(queryset, many=True)

        return Response(comment_serializer.data)
    
    def post(self, request, *args, **kwargs):
        comment_serializer = CommentSerializer(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeCommentView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            try:
                queryset = LikeComment.objects.get(pk=pk)
                serializer = LikeCommentSerializer(queryset)
                return Response(serializer.data)
            except LikeComment.DoesNotExist:
                raise Http404
        else:
            queryset = LikeComment.objects.all()
            serializer = LikeCommentSerializer(queryset, many=True)
            return Response(serializer, status=status.HTTP_200_OK)

