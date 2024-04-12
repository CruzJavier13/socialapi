from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostSerializer
from rest_framework import status
from django.http import Http404
from .models import Post

# Create your views here.
class PostView(APIView):
    
    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            try:
                queryset = Post.objects.get(pk=pk)
                serializer = PostSerializer(queryset)
                return Response(serializer.data)
            except Post.DoesNotExist:
                raise Http404
        else:
            queryset = Post.objects.all()
            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        post_serializer = PostSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

