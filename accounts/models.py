from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError("Please enter valid email")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,name,password):
        user=self.create_user(email,name,password)
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length = 100)
    total_income = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)
    uutoken=models.CharField(max_length=100,null=True,blank=True)

    objects = UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def __str__(self):
        return self.name
