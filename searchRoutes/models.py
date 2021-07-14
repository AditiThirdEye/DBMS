from django.db import models

# Create your models here.
class Flight_Routes(models.Model):
    airline = models.CharField(max_length=30)
    airline_ID = models.CharField(max_length=30)
    source_airport = models.CharField(max_length=30)
    source_airport_id = models.CharField(max_length=30)
    destination_airport = models.CharField(max_length=30)
    destination_airport_id = models.CharField(max_length=30)



'''
   airline
   airline ID
   source airport
   source airport id
   destination apirport
   destination airport id
   codeshare
   stops
   equipment
'''
