from django.db import models

# Create your models here.
class MarkedDate(models.Model):
    User_Name = models.CharField (max_length = 30,default="Unkown User")
    room = models.CharField(max_length=10,default="NA")
    date = models.DateField()
    cleaned = models.BooleanField(default=False)
