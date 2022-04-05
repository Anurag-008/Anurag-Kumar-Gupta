from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50, unique=True)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return self.name

    