from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError("No Email")
        if not username:
            raise ValueError("No username")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name = "email", max_length = 60, unique = True)
    username = models.CharField(max_length = 60, unique = True)
    date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
    last_login = models.DateTimeField(verbose_name = 'last login', auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    lat = models.FloatField(default = 0.0)
    lon = models.FloatField(default = 0.0)
    seek_text = models.TextField(max_length = 500, blank = True)
    provide = models.BooleanField(default = False)
    occupation = models.CharField(max_length=100, blank = True)
    address = models.CharField(max_length=200, blank = True)
    seek_time = models.DateTimeField(blank = True, auto_now=True, auto_now_add=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    

    