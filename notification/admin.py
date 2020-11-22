from django.contrib import admin
from .models import ConnectedUsers, SeekRequest, ProvideRequest, Notification

# Register your models here.
admin.site.register(ConnectedUsers)
admin.site.register(SeekRequest)
admin.site.register(ProvideRequest)
admin.site.register(Notification)

