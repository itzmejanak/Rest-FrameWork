from django.db import models

# Create your models here.
class ModelData(models.Model):
    name = models.CharField(max_length=20)
    roll_no = models.IntegerField()
    student_class = models.CharField(max_length=20)
    age = models.IntegerField()