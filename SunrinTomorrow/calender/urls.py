from django.urls import path
from .views import *

urlpatterns = [
    path('',main),

    path('update-data/', update_data),
    path('d-day/tests/', DDayTests.as_view()),
    path('d-day/festivals/', DDayFestivals.as_view()),
    path('d-day/holidays/', DDayHolidays.as_view()),

    path('schedules/<int:year>/', GetSchedules.as_view()),
    path('schedules/<int:year>/<int:month>/', GetSchedules.as_view()),
    path('schedules/<int:year>/<int:month>/<int:day>/', GetSchedules.as_view()),

    path('schedules/tests/<int:year>/', GetTests.as_view()),
    path('schedules/festivals/<int:year>/', GetFestivals.as_view()),
    path('schedules/holidays/<int:year>/', GetHolidays.as_view()),
    
    path('schedules/holidays/<int:year>/<int:month>/', GetHolidays.as_view()),
]