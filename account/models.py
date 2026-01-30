from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    profile_url = models.URLField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
