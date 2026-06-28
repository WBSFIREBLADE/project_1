from django.shortcuts import render
from .serializers import RegisterUserSerializer, LogoutSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
import logging

logger = logging.getLogger(__name__)

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(

                f"New user registered | username={user.username} | email={user.email}"

            )
            return Response(
                {
                "message": "User registered successfully.",

                "user": serializer.data
                },

                status=status.HTTP_201_CREATED

            )
        logger.warning(

            f"Registration failed | errors={serializer.errors}"

        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(
                f"User logged out | username={request.user.username}"
            )
            return Response(
                {"message": "Logged out successfully."},

                status=status.HTTP_200_OK

            )
        logger.warning(
            f"Logout failed | errors={serializer.errors}"
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# Create your views here.
