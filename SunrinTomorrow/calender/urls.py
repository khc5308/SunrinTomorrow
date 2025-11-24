from django.urls import path
from .views import get_schedules, get_holidays, get_tests, get_festivals, get_summary_class_days, get_all_month, put_data, update_data

urlpatterns = [
    path('schedules', get_schedules.as_view()),
    path('events/holidays', get_holidays.as_view()),
    path('events/test', get_tests.as_view()),
    path('events/festivals', get_festivals.as_view()),
    path('summary/class-days', get_summary_class_days.as_view()),
    path('all/month', get_all_month.as_view()),
    path('all/year', get_all_month.as_view()),
    path('d-day', get_all_month.as_view()),
    path('putData', put_data.as_view()),
    path('update', update_data),
]