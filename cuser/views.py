from django.shortcuts import render
from rest_framework.response import  Response
from rest_framework import  status
from .models import User
from .serializer import UserSerializer, UserLoginSerializer, UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth import authenticate
import json

# Create your views here.


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserLogin(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        ser = UserLoginSerializer(data={"email":email, "password":password})
        usr = authenticate(username=email, password=password)
        if usr:
            user = User.objects.get(email = email)
            token = get_tokens_for_user(user)
            ser = UserSerializer(user)
            return Response({"success":True, "tokens":token, "data":ser.data}, status = status.HTTP_200_OK)
        else:
            return Response({'error': ser.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserRegister(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        data = request.data
        data = json.dumps(data)
        data = json.loads(data)
        ser = UserRegisterSerializer(data=data)
        if ser.is_valid():
            ser.save()
            usr = User.objects.get(email=email)
            usr.set_password(password)
            usr.save()
            return Response({'data':ser.data    }, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': ser.errors}, status=status.HTTP_400_BAD_REQUEST)