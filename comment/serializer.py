from rest_framework import serializers
from .models import CommentPost, LikeComment, LikePost

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model=CommentPost
        fields='__all__'

class LikeCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model=LikeComment
        fields = '__all__'

class LikePostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=LikePost
        fields='__all__'