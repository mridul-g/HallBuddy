from django.db import models

# Create your models here.
class Guestroom(models.Model):

    room = models.CharField(max_length=5)

    #status choices
    BOOK = 'book'
    UNAVAILABLE = 'unavailable'

    STATUS_CHOICES = [
        (BOOK,'Book'),
        (UNAVAILABLE, 'Item is Booked')
    ]

    status = models.CharField(
        max_length=100,
        choices = STATUS_CHOICES
    )
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    type=models.CharField(max_length=100,default="Standard Room")
    price = models.CharField(max_length=100)
    manager_validation = models.CharField(max_length=10,default='NO')


    #Essentials
    date = models.DateField()
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    room = models.CharField(max_length=5)
    type=models.CharField(max_length=100,default="Standard Room")
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.room