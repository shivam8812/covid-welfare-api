from rest_framework import serializers

from .models import User1

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User1
        fields = ['email', 'name', 'latitude', 'longitude', 'blood_group', 'occupation']