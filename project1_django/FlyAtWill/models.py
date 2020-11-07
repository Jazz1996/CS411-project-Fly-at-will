from django.db import models


# Create your models here.
class Airport(models.Model):
    objects = models.Manager()
    iatacode = models.CharField(db_column='IATACode', primary_key=True, max_length=3)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Airport'


class Flight(models.Model):
    objects = models.Manager()
    flightno = models.CharField(db_column='FlightNo', primary_key=True, max_length=10)  # Field name made lowercase.
    airlinecode = models.CharField(db_column='AirlineCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    deptiata = models.CharField(db_column='DeptIATA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    arriata = models.CharField(db_column='ArrIATA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    depttime = models.TimeField(db_column='DeptTime', blank=True, null=True)  # Field name made lowercase.
    arrtime = models.TimeField(db_column='ArrTime', blank=True, null=True)  # Field name made lowercase.
    aircraft = models.CharField(db_column='Aircraft', max_length=20, blank=True, null=True)  # Field name made lowercase.
    distance = models.IntegerField(db_column='Distance', blank=True, null=True)  # Field name made lowercase.
    otd = models.CharField(db_column='OTD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    avgdelay = models.IntegerField(db_column='AvgDelay', blank=True, null=True)  # Field name made lowercase.
    monday = models.IntegerField(db_column='Monday', blank=True, null=True)  # Field name made lowercase.
    tuesday = models.IntegerField(db_column='Tuesday', blank=True, null=True)  # Field name made lowercase.
    wednesday = models.IntegerField(db_column='Wednesday', blank=True, null=True)  # Field name made lowercase.
    thursday = models.IntegerField(db_column='Thursday', blank=True, null=True)  # Field name made lowercase.
    friday = models.IntegerField(db_column='Friday', blank=True, null=True)  # Field name made lowercase.
    saturday = models.IntegerField(db_column='Saturday', blank=True, null=True)  # Field name made lowercase.
    sunday = models.IntegerField(db_column='Sunday', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Flight'
