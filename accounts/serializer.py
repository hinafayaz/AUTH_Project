from rest_framework import serializers
from .models import User,AuthTokens

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password', 'firstname','lastname','email']



