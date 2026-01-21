from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Promocode(models.Model):
    code = models.TextField()
    # user = models.ForeignKey('user.username', on_delete=models.CASCADE)
    def __str__(self):
        return self.code
