from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=55)
    roll=models.IntegerField(blank=True, null=True)
    city=models.CharField(max_length=55)
      