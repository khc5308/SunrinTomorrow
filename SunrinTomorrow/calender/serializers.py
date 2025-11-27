from rest_framework import serializers
from .models import Schedules,Summary

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = ['year', 'month', 'week', 'day', 'title', 'name']

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ['grade']
