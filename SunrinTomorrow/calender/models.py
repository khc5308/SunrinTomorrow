from django.db import models

# Create your models here.

class Schedules(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField(null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)

class Events(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    month = models.IntegerField(null=True, blank=True)    

class AllData(models.Model):
    year = models.IntegerField()
    month = models.IntegerField(null=True, blank=True)

class Summary(models.Model):
    grade = models.IntegerField()

class Update_data(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    title = models.CharField(max_length=100)
    name = models.TextField()