from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import datetime

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from account.models import User
from .models import SeekRequest, ConnectedUsers, ProvideRequest

class SeekView(ModelViewSet):
    queryset = SeekRequest.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def connect(self, user1, user2):
        self.connect_util(user1, user2)
        self.connect_util(user2, user1)

    def connect_util(self, user, to_user):
        connections = ConnectedUsers.objects.get(user = user)
        connections.connected.add(to_user)
        connections.save()

    def seek_request(self, request):
        user = request.user
        to_user = User.objects.get(username = request.data['user'])

        connectlist = ConnectedUsers.objects.get(user = user)

        if to_user in connectlist.connected.all():
            return Response({'already connected'})

        try:
            seek_r = SeekRequest.objects.get(seeker = user, provider = to_user)
            return Response({'request already sent'})
        except SeekRequest.DoesNotExist:
            try:
                prov = ProvideRequest.objects.get(seeker = user, provider = to_user)
                self.connect(user, to_user)
                prov.delete()
                return Response({'users connected'})
            except ProvideRequest.DoesNotExist:
                seek_r = SeekRequest(seeker = user, provider = to_user)
                seek_r.save()
                return Response({'request sent'})


    def seek_request_list(self, request):
        quer = SeekRequest.objects.filter(seeker = request.user)
        response = []

        for j in quer:
            response.append(j.provider.username)

        return Response({'users':response})


    def delete_request(self, request):
        to_user = User.objects.get(username = request.data['user'])
        try:
            seek_r = SeekRequest.objects.get(seeker = request.user, provider = to_user)
            seek_r.delete()
            return Response({'successfully deleted'})
        except SeekRequest.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def cancel_request(self, request):
        to_user = User.objects.get(username = request.data['user'])
        try:
            seek_r = SeekRequest.objects.get(provider = request.user, seeker = to_user)
            seek_r.delete()
            return Response({'successfully cancelled'})
        except SeekRequest.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
                    

        


        

    