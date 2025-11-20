from django.urls import path
from .views import get_schedules, get_holidays, get_tests, get_festivals, get_summary_class_days, get_all_month, put_data, update_data

urlpatterns = [
    path('schedules', get_schedules),
    path('events/holidays', get_holidays),
    path('events/test', get_tests),
    path('events/festivals', get_festivals),
    path('summary/class-days', get_summary_class_days),
    path('all/month', get_all_month),
    path('all/year', get_all_month),
    path('d-day', get_all_month),
    path('putData', put_data),
    path('update', update_data),
]