from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import datetime

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from account.models import User
from .models import SeekRequest, ConnectedUsers, ProvideRequest, Notification

class ProvideView(ModelViewSet):
    queryset = ProvideRequest.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def connect(self, user1, user2):
        self.connect_util(user1, user2)
        self.connect_util(user2, user1)

    def connect_util(self, user, to_user):
        connections = ConnectedUsers.objects.get(user = user)
        connections.connected.add(to_user)
        connections.save()

    def provide_request(self, request):
        user = request.user
        to_user = User.objects.get(username = request.data['user'])

        connectlist = ConnectedUsers.objects.get(user = user)

        if to_user in connectlist.connected.all():
            
            return Response({'already connected'})

        try:
            provide_r = ProvideRequest.objects.get(seeker = to_user, provider = user)
            return Response({'request already sent'})
        except ProvideRequest.DoesNotExist:
            try:
                seek_r = SeekRequest.objects.get(seeker = to_user, provider = user)
                self.connect(user, to_user)
                seek_r.delete()
                notify = Notification(user = user, notification = str(to_user.username) + " is connected")
                notify.save()
                notify = Notification(user = to_user, notification = str(user.username) + " is connected")
                notify.save()
                return Response({'users connected'})
            except SeekRequest.DoesNotExist:
                provide_r = ProvideRequest(seeker = to_user, provider = user)
                provide_r.save()
                notify = Notification(user = to_user, notification = str(user.username) + " is ready to help")
                notify.save()
                return Response({'request sent'})


    def provide_request_list(self, request):
        quer = ProvideRequest.objects.filter(provider = request.user)
        response = []

        for j in quer:
            response.append(j.seeker.username)

        return Response({'users':response})


    def delete_request(self, request):
        to_user = User.objects.get(username = request.data['user'])
        try:
            seek_r = ProvideRequest.objects.get(provider = request.user, seeker = to_user)
            seek_r.delete()
            return Response({'successfully deleted'})
        except ProvideRequest.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def cancel_request(self, request):
        to_user = User.objects.get(username = request.data['user'])
        try:
            seek_r = ProvideRequest.objects.get(seeker = request.user, provider = to_user)
            seek_r.delete()
            return Response({'successfully cancelled'})
        except ProvideRequest.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

                    

        


        

    