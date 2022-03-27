from rest_framework import serializers
from .models import Posts,Comments


class CreatePostSerializer(serializers.Serializer):
    Title=serializers.CharField(max_length=500)
    Description=serializers.CharField(max_length=10000000) 

class CommentSerializer(serializers.Serializer):
    Comment=serializers.CharField(max_length=1000000)

