from django.db import models

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70,unique=True)
    mobile=models.CharField(max_length=70,unique=True)