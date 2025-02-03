from django.db import models

# Create your models here.
class studentsInfo(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    is_active = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.name