from django.shortcuts import render, get_object_or_404
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
    
    def put(self, request, pk=None, *args, **kwargs):
        instance = get_object_or_404(CommentPost, pk=pk)
        comment_serializer = CommentSerializer(instance, data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_200_OK)
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        """
        comment_serializer = CommentSerializer(request.data)
        if comment_serializer.is_valid():
            comment_serializer.update()
            return Response(request.data, status=status.HTTP_200_OK)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        """
    
    def delete(self, request, pk=None, *args, **kwargs):
        instance = get_object_or_404(CommentPost, pk=pk)
        if instance:
            instance.delete()
        return Response({"Message":f"deleted comment {pk}"}, status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(CommentPost, pk=pk)
        comment_serializer = CommentSerializer(instance, request.data, partial=True)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(request.data, status=status.HTTP_200_OK)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
    
class LikePostView(APIView):

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            try:
                queryset = LikePost.objects.get(pk=pk)
                serializer = LikePostSerializer(queryset)
            except LikePost.DoesNotExist:
                raise Http404
        else:
            queryset = LikePost.objects.all()
            serializer = LikePostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        likepost_serializer = LikePostSerializer(request.data)
        if likepost_serializer.is_valid():
            likepost_serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
        

class LikeCommentView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            try:
                queryset = LikeComment.objects.get(pk=pk)
                serializer = LikeCommentSerializer(queryset)
            except LikeComment.DoesNotExist:
                raise Http404
        else:
            queryset = LikeComment.objects.all()
            serializer = LikeCommentSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        likecomment_serializer = LikeCommentSerializer(request.data)
        if likecomment_serializer.is_valid():
            likecomment_serializer.save()
            return Response(likecomment_serializer.data, status=status.HTTP_201_CREATED)
        return Response(LikeCommentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


