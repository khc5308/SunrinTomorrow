from django.db import models

# Create your models here.

class schedules(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    week = models.IntegerField()
    