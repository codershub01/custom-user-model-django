from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import   datetime
# Create your models here.

class UserManager(BaseUserManager):
    def create(self, email, password='', **other_fields):
        if not email:
            raise ValueError("User should have a email address")
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        user = self.model(email=email, password=password, **other_fields)
        user.last_login = datetime.now()
        user.save()
        return user

class User(AbstractBaseUser):



    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254,unique=True)
    password = models.CharField(max_length=128)
    city = models.CharField(max_length=60)
    contact = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()


    USERNAME_FIELD = 'email'