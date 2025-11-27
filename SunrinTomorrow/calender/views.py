import csv
import datetime
from .models import Schedules
from .serializers import ScheduleSerializer

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

@api_view(['GET'])
def main(request):
    return Response({"message": "Hello"}, status=status.HTTP_200_OK)

class GetSchedules(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        
        queryset = Schedules.objects.filter(year=year)
        
        if month:
            queryset = queryset.filter(month=month)
        if day:
            queryset = queryset.filter(day=day)

            
        return queryset

class BaseEventListView(generics.ListAPIView):
    serializer_class = ScheduleSerializer
    event_title = None

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')

        queryset = Schedules.objects.filter(year=year, title=self.event_title)
        
        if month:
            queryset = queryset.filter(month=month)
            
        return queryset

class GetTests(BaseEventListView):
    event_title = "test"

class GetFestivals(BaseEventListView):
    event_title = "festival"

class GetHolidays(BaseEventListView):
    event_title = "holidays"

class BaseDDay(APIView):
    event_title = None

    def get(self, request):
        today = datetime.date.today()
        
        if self.event_title:
            candidates = Schedules.objects.filter(year__gte=today.year, title=self.event_title)
        else:
            candidates = Schedules.objects.filter(year__gte=today.year)

        upcoming_events = []
        
        for schedule in candidates:
            try:
                event_date = datetime.date(schedule.year, schedule.month, schedule.day)
                
                if event_date >= today:
                    days_left = (event_date - today).days
                    upcoming_events.append({
                        'name': schedule.name,
                        'date': event_date,
                        'd-day': days_left
                    })
            except ValueError:
                continue

        if not upcoming_events:
            return Response({'message': '예정된 일정이 없습니다.'}, status=status.HTTP_200_OK)

        upcoming_events.sort(key=lambda x: x['d-day'])
        
        nearest_event = upcoming_events[0]
        
        return Response(nearest_event, status=status.HTTP_200_OK)

class DDayTests(BaseDDay):
    event_title = "test"
class DDayFestivals(BaseDDay):
    event_title = "festival"
class DDayHolidays(BaseDDay):
    event_title = "holidays"

@api_view(['POST'])
def update_data(request):
    try:
        with open("calender/data.csv", "r", encoding="utf-8") as f:
            data = csv.DictReader(f)
            
            Schedules.objects.all().delete()
            
            count = 0
            for item in data:
                date_str = item['date'].strip()
                year = int(date_str[:4])
                month = int(date_str[4:6])
                day = int(date_str[6:])
                
                title = item['title'].strip()
                name = item['name'].strip()
                
                
                dt = datetime.date(year, month, day)
                week = dt.isocalendar()[1]

                Schedules.objects.create(
                    year=year,
                    month=month,
                    day=day,
                    week=week,
                    title=title,
                    name=name
                )
                count += 1
            
        return Response({'message': f' {count}개의 데이터 생성'}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)