from django.db import models

# Create your models here.
class MarkedDate(models.Model):
    date = models.DateField()
    cleaned = models.BooleanField(default=False) 
