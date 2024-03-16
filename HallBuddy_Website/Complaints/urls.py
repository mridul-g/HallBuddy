from django.urls import path
from . import views

urlpatterns = [
    
    # students
    path('Pending_Request', views.Pending_Request, name='Pending_Request'),
    path('Past_Request', views.Past_Request, name='Past_Request'),
    path('Lodge_Request',views.Lodge_Request, name='Lodge_Request'),
    
    # hall manager
    path('Complaints_hall', views.Complaints_hall, name='Complaints_hall'),
    
]