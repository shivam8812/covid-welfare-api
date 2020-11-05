from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import RegistrationSerializer
from .models import User
from rest_framework.authtoken.models import Token


class AuthenticationView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user = user).key
            return Response({'success':'registered', 'token':token})
        else :
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

