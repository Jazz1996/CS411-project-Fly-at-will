from django.db import models

# Create your models here.
class djangoAirline(models.Model):
    FlightNo = models.CharField(primary_key=True,max_length=10)
    AirlineCode = models.CharField(max_length=2)
    DeptIATA = models.CharField(max_length=3)
    ArrIATA = models.CharField(max_length=3)
    DeptTime = models.TimeField()
    ArrTime = models.TimeField()
    Aircraft = models.CharField(max_length=15)
    Distance = models.IntegerField()
    OTD = models.CharField(max_length=5)
    AvgDelay = models.IntegerField()
    Monday = models.BooleanField(default=True)
    Tuesday = models.BooleanField(default=True)
    Wednesday = models.BooleanField(default=True)
    Thursday = models.BooleanField(default=True)
    Friday = models.BooleanField(default=True)
    Saturday = models.BooleanField(default=True)
    Sunday = models.BooleanField(default=True)
    class Meta:
        db_table = 'djangoAirline'
