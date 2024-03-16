from django.urls import path
from . import views

urlpatterns = [
    path("", views.calendar_view, name='calendar'),
    path("mark_date", views.mark_date, name="mark_date"),
    path("get_marked_dates", views.get_marked_dates, name="get_marked_dates"),
]