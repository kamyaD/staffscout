from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class User(AbstractUser):
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=215, blank=True)
    country=models.CharField(max_length=215, blank=True)
    job_title =models.CharField(max_length=215, blank=True)
    availability_status = models.CharField(max_length=215, blank=True)
    profile_pic = models.ImageField(blank=True)
    password2 = models.CharField(max_length=215, blank=True)
    



    def __str__(self):
        return self.username
    