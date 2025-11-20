from rest_framework import serializers
from .models import Schedules, Events, AllData, Summary, Update_data

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = ['year', 'month', 'day', 'week']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['title', 'year', 'month']
    
class AllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllData
        fields = ['year', 'month']

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ['grade']

class UpdateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update_data
        fields = ['year', 'month', 'day']