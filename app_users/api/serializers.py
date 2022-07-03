from rest_framework import serializers
from app_users.models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['user_type',]
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model=User
        fields=['username', 'email', 'password','profile']