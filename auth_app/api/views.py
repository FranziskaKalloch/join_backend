from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import SignUpSerializer



class SignUpView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        """Validates registration data, creates a user, and returns HTTP 201."""
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        full_name = user.get_full_name()
        return Response({"full_name": full_name, "email": user.email}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    pass
