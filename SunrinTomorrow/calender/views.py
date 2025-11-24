import csv
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Schedules, Events, Summary, Update_data, AllData
from .serializers import ScheduleSerializer, EventSerializer, AllDataSerializer, SummarySerializer, UpdateDataSerializer

import datetime

class get_schedules(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        if self.kwargs.get('week') is None:
            return Schedules.objects.filter(year=year, month=month)
        else:
            week = self.kwargs['week']
        
        if day is None:
            return Schedules.objects.filter(year=year, month=month, week=week)
        else:
            day = self.kwargs['day']
        return Schedules.objects.filter(year=year, month=month, week=week, day=day)
    
class BaseEventListView(generics.ListAPIView):
    serializer_class = EventSerializer
    event_title = None

    def get_queryset(self):
        year = self.kwargs['year']
        return Events.objects.filter(
            year=year,
            title=self.event_title
            # 이거 각각 클래스로 할거면
            # title = 'AJR' 이렇게 고정해도됨
        )

class get_tests(BaseEventListView):
    event_title = "test"

class get_festivals(BaseEventListView):
    event_title = "festival"

class get_holidays(BaseEventListView):
    event_title = "holiday"

    def get(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        return Events.objects.filter(
            year=year,
            month=month,
            title=self.event_title
        )
    
class get_summary_class_days(generics.RetrieveAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer
    lookup_field = 'grade'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class get_all_month(generics.ListAPIView):
    queryset = AllData.objects.all()
    serializer_class = AllDataSerializer

    def get(self):
        return self.list(self)

class get_all_year(generics.ListAPIView):
    queryset = AllData.objects.all()
    serializer_class = AllDataSerializer

    def get(self):
        return self.list(self)

class get_summary_class_days(generics.RetrieveAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer
    lookup_field = 'grade'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class get_all_month(generics.ListAPIView):
    queryset = AllData.objects.all()
    serializer_class = AllDataSerializer
    lookup_field = 'month'

    def get(self):
        return self.list(self)

class get_all_year(generics.ListAPIView):
    queryset = AllData.objects.all()
    serializer_class = AllDataSerializer
    lookup_field = 'year'

    def get(self):
        return self.list(self)

class put_data(generics.UpdateAPIView):
    queryset = Update_data.objects.all()
    serializer_class = UpdateDataSerializer

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

@api_view(['GET'])
def d_day(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        for i in Events.objects.all():
            if i.year >= now.year and i.month >= now.month:
                event_date = datetime.datetime(i.year, i.month, 1)
                delta = event_date - now
                return Response({'d-day': delta.days}, status=status.HTTP_200_OK)
            
@api_view(['POST'])
def update_data(request):
    if request.method == 'POST':
        with open("calender/data.csv", "r", encoding="utf-8") as f:
            data = csv.DictReader(f)
            for item in data:
                year = item['date'][:4]
                month = item['date'][4:6]
                day = item['date'][6:]
                title = item['title']
                name = item['name']
                obj, created = Update_data.objects.create(
                    year=year,
                    month=month,
                    day=day,
                    title=title,
                    name=name
                )
        return Response({'message': 'Data updated successfully'}, status=status.HTTP_200_OK)