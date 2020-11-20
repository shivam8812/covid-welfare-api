from django.db import models
from django.conf import settings

# Create your models here.
class ConnectedUsers(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "user")
    connected = models.ManyToManyField(settings.AUTH_USER_MODEL, blank = True, related_name = "connections")

    def __str__(self):
        return self.user.username
    

class SeekRequest(models.Model):
    seeker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'seeker')
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'provider')
    request_time = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.seeker.username + ' -> ' + self.provider.username

class ProvideRequest(models.Model):
    seeker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'seeker_provide')
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'provider_provide')
    request_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.provider.username + ' -> ' + self.seeker.username
    