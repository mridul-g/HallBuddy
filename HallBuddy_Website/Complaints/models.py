from django.db import models
from django import forms

class Complaint_Request (models.Model):
    # An instance is generated when a request is raised by any user
    User_Name = models.CharField (max_length = 30) #check maxlength later
    location = models.TextField(max_length=15,default="Not Given")
    Done = models.BooleanField(default=False)
    Place = models.CharField(max_length=10,default="Not Given")
    category=models.CharField(max_length=20,default="Not Given")
    sub_category=models.CharField(max_length=20,default="Not Given")
    comments = models.TextField(max_length=200)
    Complaint_DateTime = models.DateTimeField()
    
