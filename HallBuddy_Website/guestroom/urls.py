from django.urls import path
from guestroom import views

urlpatterns = [
    
    # students
    path('book', views.guestroom, name='guestroom'),
    path('pastbookings', views.pastbookings, name='pastbookings'),
    # hall manager
    path('pending', views.pending, name='pending'),
    path('aprooved', views.bookings_aprooved, name='bookings_aprooved'),


    # path('return_request_initiate', views.return_request_initiate, name='return_request_initiate')
]