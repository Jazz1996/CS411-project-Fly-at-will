# Generated by Django 3.1.3 on 2020-11-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0002_auto_20201107_0250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('iatacode', models.CharField(db_column='IATACode', max_length=3, primary_key=True, serialize=False)),
                ('city', models.CharField(blank=True, db_column='City', max_length=30, null=True)),
                ('latitude', models.FloatField(blank=True, db_column='Latitude', null=True)),
                ('longitude', models.FloatField(blank=True, db_column='Longitude', null=True)),
            ],
            options={
                'db_table': 'Airport',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flightno', models.CharField(db_column='FlightNo', max_length=10, primary_key=True, serialize=False)),
                ('airlinecode', models.CharField(blank=True, db_column='AirlineCode', max_length=2, null=True)),
                ('deptiata', models.CharField(blank=True, db_column='DeptIATA', max_length=3, null=True)),
                ('arriata', models.CharField(blank=True, db_column='ArrIATA', max_length=3, null=True)),
                ('depttime', models.TimeField(blank=True, db_column='DeptTime', null=True)),
                ('arrtime', models.TimeField(blank=True, db_column='ArrTime', null=True)),
                ('aircraft', models.CharField(blank=True, db_column='Aircraft', max_length=20, null=True)),
                ('distance', models.IntegerField(blank=True, db_column='Distance', null=True)),
                ('otd', models.CharField(blank=True, db_column='OTD', max_length=10, null=True)),
                ('avgdelay', models.IntegerField(blank=True, db_column='AvgDelay', null=True)),
                ('monday', models.IntegerField(blank=True, db_column='Monday', null=True)),
                ('tuesday', models.IntegerField(blank=True, db_column='Tuesday', null=True)),
                ('wednesday', models.IntegerField(blank=True, db_column='Wednesday', null=True)),
                ('thursday', models.IntegerField(blank=True, db_column='Thursday', null=True)),
                ('friday', models.IntegerField(blank=True, db_column='Friday', null=True)),
                ('saturday', models.IntegerField(blank=True, db_column='Saturday', null=True)),
                ('sunday', models.IntegerField(blank=True, db_column='Sunday', null=True)),
            ],
            options={
                'db_table': 'Flight',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='djangoAirline',
        ),
    ]
