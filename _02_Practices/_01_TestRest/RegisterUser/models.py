from django.db import models

# Create your models here.
class RegisterUser(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name