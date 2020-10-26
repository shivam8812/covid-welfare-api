from django.db import models
from django import forms

# Create your models here.

class User1(models.Model):
    name = models.CharField(unique = True, max_length = 100, blank = True, default = '')
    latitude = models.FloatField()
    longitude = models.FloatField()
    blood_group = models.CharField(max_length = 3, blank = True, default = '')
    occupation = models.CharField(max_length = 100, blank = True, default = '')
    address = models.CharField(max_length = 200, blank = True, default = '')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    email = models.EmailField(max_length = 254)
    status = models.BooleanField()
    seek_text = models.TextField()
    date_seek = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


