from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SnakeLeaderboard(models.Model):
    user = models.CharField(max_length=50, primary_key = True)
    score = models.IntegerField()

class ClickerLeaderboard(models.Model):
    user = models.CharField(max_length=50, primary_key = True)
    score = models.IntegerField()

class GalagaLeaderboard(models.Model):
    user = models.CharField(max_length=50, primary_key = True)
    score = models.IntegerField()