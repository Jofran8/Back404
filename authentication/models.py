from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    telephone = models.CharField(null=True, max_length=9)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email

    def create_user(self, **kwargs):
        user = self.model(
            username=kwargs['username'],
            email=self.normalize_email(kwargs['email'])
        )
        user.set_password(kwargs['password'])
        user.save()
        return user

    def tokens(self):
        token = RefreshToken.for_user(self)
        return {
            'refresh_token': str(token),
            'access_token': str(token.access_token)
        }
