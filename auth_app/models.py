from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)
    phone = models.CharField(max_length=50, blank=True)
    
    USERNAME_FIELD = "email" # legt fest, welches Feld DJango zur Idendifikation beim Anmelden verwendet    
    REQUIRED_FIELDS = [
        "first_name", 
        "last_name", 
    ]
    
    objects = UserManager()
    
    def __str__(self):
        return self.first_name + " " +self.last_name