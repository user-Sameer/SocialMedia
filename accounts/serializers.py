
from django.contrib.auth import get_user_model
from .models import UserFollowing
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')


class GetUserFollowingSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100)
    followers= serializers.IntegerField()
    following= serializers.IntegerField()
