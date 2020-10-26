from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import User1
from .serializers import UserDetailSerializer

class UserDetailView(ModelViewSet):
    queryset = User1.objects.all()
    serializer_class = UserDetailSerializer

    def get(self, request, username):
        try:
            return User1.objects.get(name = slug)
        except User1.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        



