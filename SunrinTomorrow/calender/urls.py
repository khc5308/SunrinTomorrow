# urls.py 예시
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),

    path('update-data/', views.update_data),
    path('d-day/tests/', views.DDayTests.as_view()),
    path('d-day/festivals/', views.DDayFestivals.as_view()),
    path('d-day/holidays/', views.DDayHolidays.as_view()),

    path('schedules/<int:year>/', views.GetAllYear.as_view()),
    path('schedules/<int:year>/<int:month>/', views.GetAllMonth.as_view()),
    path('schedules/<int:year>/<int:month>/<int:day>/', views.GetSchedules.as_view()),

    path('schedules/tests/<int:year>/', views.GetTests.as_view()),
    path('schedules/festivals/<int:year>/', views.GetFestivals.as_view()),
    path('schedules/holidays/<int:year>/', views.GetHolidays.as_view()),
    
    path('schedules/holidays/<int:year>/<int:month>/', views.GetHolidays.as_view()),

    #path('summary/<int:grade>/', views.GetSummaryClassDays.as_view()),
]