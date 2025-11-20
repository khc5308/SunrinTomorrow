from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .models import Schedule, Holiday, Test, Festival
from .serializers import ScheduleSerializer, HolidaySerializer, TestSerializer, FestivalSerializer