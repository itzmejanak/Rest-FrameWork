from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    is_active = models.CharField(max_length=3)
    def __str__(self) -> str:
        return self.name
