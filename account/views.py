from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import RegistrationSerializer
from .models import User

class AuthenticationView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'success':'registered'})
        else :
            return Response(serializer.errors)

