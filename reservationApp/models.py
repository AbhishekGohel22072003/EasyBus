from re import I
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from more_itertools import quantify
from django.db.models import Sum
from django.contrib.auth.models import User
from datetime import time
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    location = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location

class Bus(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    bus_number = models.CharField(max_length=250)
    seats = models.IntegerField(default=0)  # Changed from FloatField to IntegerField
    isDaily = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=(('1', 'Active'), ('2', 'Inactive')), default='1')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bus_number
    


# This table has to be added in REVISED Documentation
class Seats(models.Model):
    owner = models.ForeignKey(User,on_delete=models.Case,default=None,null=True)
    seat_number = models.IntegerField(default=0)
    is_booked = models.BooleanField(default=False)
    
    # The following we have to implement for noting down time of the ticket booked
    # To be added in the screen shot in REVISED documentation
    timeStamp = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.id}"

class Schedule(models.Model):
    code = models.CharField(max_length=100)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seats,related_name="seats")
    
    via = models.ManyToManyField(Location,name="via")
    depart = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='depart_location')
    destination = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='destination')
    schedule= models.DateTimeField()    
    fare= models.FloatField()
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Cancelled')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    # This is for the time taken by the bus to complete the trip from the source to destination
    # This will also be added in REVISED documentation
    # time = models.TimeField(default=time)
    

    def __str__(self):
        return str(self.code + ' - ' + self.bus.bus_number + " - " + str(self.id))
    
    def count_available(self):
        booked = Booking.objects.filter(schedule=self).aggregate(Sum('seats'))['seats__sum']
        seats = self.bus.seats
        if seats is not None:
            if booked is not None:
                return seats - booked
            else:
                return seats
        else:
            return 0  # Or any default value you prefer



    


class Booking(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=1,related_name='user_booking')
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE)
    seats = models.IntegerField(default=0)
    fare = models.FloatField(default=0.0)
    book_seats = models.ManyToManyField(Seats,related_name="book_seats")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.code + ' - ' + self.name)

    def total_payable(self):
        return self.seats * self.schedule.fare