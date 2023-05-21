from django.db import models

# Create your models here.

class record(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.CharField(max_length=20)
