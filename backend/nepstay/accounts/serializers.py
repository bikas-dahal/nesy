from rest_framework import serializers

from .models import Profile

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email'
        )

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Profile
        fields = (
            'id', 'avatar_url', 'user'
        )