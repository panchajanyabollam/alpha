from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    phone_number = models.CharField(
        max_length=15, 
        unique=True, 
        null=True, 
        blank=True,
        help_text="Phone number must be unique"
    )
    email = models.EmailField(
        unique=True,
        help_text="Email address must be unique"
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
