from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserScore(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    snakeScore = models.IntegerField()#decimal_places=10, max_digits=10