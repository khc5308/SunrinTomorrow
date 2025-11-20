from django.db import models

# Create your models here.

class schedules(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField(null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)

class events(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    month = models.IntegerField(null=True, blank=True)    

class allData(models.Model):
    year = models.IntegerField()
    month = models.IntegerField(null=True, blank=True)

class summary(models.Model):
    grade = models.IntegerField()

class Update_data(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()