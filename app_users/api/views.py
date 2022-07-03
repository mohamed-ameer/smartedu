from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView

class SignupView(generics.GenericAPIView):
    serializer_class=UserSerializer 
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "profile":Profile.objects.get(user=user).user_type,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })
