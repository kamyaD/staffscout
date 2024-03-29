from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
import uuid


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password2 = models.CharField(max_length=215, blank=True)
    is_employer= models.BooleanField(blank=True, default=False)
    is_candidate= models.BooleanField(blank=True, default=False)
    is_both_employer_and_candidate= models.BooleanField(blank=True, default=False)

    def __str__(self):
        return f'{self.id}'


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    print("email",reset_password_token.user.email)

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Staff scouts Account"),
        # message:
        "You resently requested for a password change for Staff Scouts Account. Follow this link to reset the password:" + email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )



    def __str__(self):
        return self.id
    