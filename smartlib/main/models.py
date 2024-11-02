from django.db import models

# main/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add any additional fields you need here
    pass

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    synopsis = models.TextField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title
