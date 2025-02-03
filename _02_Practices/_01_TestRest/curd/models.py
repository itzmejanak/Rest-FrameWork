from django.db import models

class CurdClass(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    city = models.CharField(max_length=50)
    stats = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.name} - Roll No: {self.roll_no}"