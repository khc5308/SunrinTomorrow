from rest_framework import generics

from .models import Schedules, Events, Alldata, Summary, Update_data
from .serializers import ScheduleSerializer, EventSerializer, AllDataSerializer, SummarySerializer, UpdateDataSerializer

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