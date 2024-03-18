from django.urls import path
from . import views

urlpatterns = [

    path ('', views.Make_Homepage, name = 'Home') ,
    path('map', views.map, name = 'map'),
    path('contact', views.contact, name = 'contact'),
    path('shop', views.shop, name = 'shop'),
    path('dues', views.dues, name = 'dues'),
]