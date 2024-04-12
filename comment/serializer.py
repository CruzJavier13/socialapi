from rest_framework import serializers
from .models import CommentPost

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model=CommentPost
        fields='__all__'