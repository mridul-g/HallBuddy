from django.db import models

# Create your models here.
class Announcement(models.Model):
    Announcement_Date = models.DateField(blank=True, null = True, default="")
    Item_Name = models.CharField(max_length=50,blank=True, null = True, default="")