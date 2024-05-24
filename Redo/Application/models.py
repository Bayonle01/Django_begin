from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 100)
    Class = models.CharField(max_length = 100)
    age = models.CharField(max_length = 100)
    performance = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 100)
    height = models.CharField(max_length = 100)
    