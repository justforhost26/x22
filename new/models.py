from django.db import models

# Create your models here.
from django.db.models import Model


class reg(Model):
    name=models.CharField(max_length=200)
    number=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=200)

