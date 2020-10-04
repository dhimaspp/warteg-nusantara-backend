from django.db import models
from django.contrib.auth.models import User  # pylint: disable=imported-auth-user
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length=254, null=True, blank=True)
    pp = models.BinaryField(null=True, blank=True)
