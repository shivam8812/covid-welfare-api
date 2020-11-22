from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import datetime

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from account.models import User
from .models import SeekRequest, ConnectedUsers, ProvideRequest, Notification

class NotificationView(ModelViewSet):
    queryset = Notification.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_notification(self, request):
        user = request.user
        notify = Notification.objects.filter(user = user)
        response = []
        for j in notify:
            response.append({'text':j.notification, 'time':j.time_request})
            pass

        return Response({"notifications":response})
