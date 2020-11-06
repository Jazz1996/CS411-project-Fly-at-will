from django.db import models


# Create your models here.
class Flight(models.Model):
    objects = models.Manager()
    deptcity = models.CharField(db_column='DeptCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    arrcity = models.CharField(db_column='ArrCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numbers = models.CharField(db_column='Numbers', primary_key=True, max_length=10)  # Field name made lowercase.
    airlines = models.CharField(db_column='Airlines', max_length=5, blank=True, null=True)  # Field name made lowercase.
    flightdate = models.DateField(db_column='FlightDate', blank=True, null=True)  # Field name made lowercase.
    depttime = models.TimeField(db_column='DeptTime', blank=True, null=True)  # Field name made lowercase.
    arrtime = models.TimeField(db_column='ArrTime', blank=True, null=True)  # Field name made lowercase.
    deptiata = models.CharField(db_column='DeptIATA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    arriata = models.CharField(db_column='ArrIATA', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Flight'
