from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserScores(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    snakeScore = models.DecimalField(decimal_places=4, max_digits=4)