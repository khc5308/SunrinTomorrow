from django.db import models

# Create your models here.

class Schedules(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    week = models.IntegerField()
    title = models.CharField(max_length=100)
    name = models.TextField()

class Summary(models.Model):
    grade = models.IntegerField()