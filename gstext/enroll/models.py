from django.db import models

# Create your models here.

class student(models.Model):
    student_name=models.CharField(max_length=100)
    student_roll=models.IntegerField()