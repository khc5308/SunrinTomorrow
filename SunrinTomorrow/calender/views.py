from django.shortcuts import render

from rest_framework import generics

from .models import Schedules, Events, Alldata, Summary, Update_data
from .serializers import ScheduleSerializer, EventSerializer, AllDataSerializer, SummarySerializer, UpdateDataSerializer

#region 스케줄
class get_schedules_day(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        week = self.kwargs['week']
        day = self.kwargs['day']
        return Schedules.objects.filter(year=year, month=month, week=week, day=day)

class get_schedules_week(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        week = self.kwargs['week']
        return Schedules.objects.filter(year=year, month=month, week=week)

class get_schedules_month(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        return Schedules.objects.filter(year=year, month=month)
    
#endregion
#region 이벤트
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
    event_title = "holiday";

    def get_queryset(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        return Events.objects.filter(
            year=year,
            month=month,
            title=self.event_title
        )
    
#endregion
#region 정보
class get_summary_class_days(generics.RetrieveAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer
    lookup_field = 'grade'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class get_all_month(generics.ListAPIView):
    queryset = Alldata.objects.all()
    serializer_class = AllDataSerializer

    def get(self):
        return self.list(self)

class get_all_year(generics.ListAPIView):
    queryset = Alldata.objects.all()
    serializer_class = AllDataSerializer

    def get(self):
        return self.list(self)
    
#endregion
