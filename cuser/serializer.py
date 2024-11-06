from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['password']