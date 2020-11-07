# Generated by Django 3.1.3 on 2020-11-06 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoAirline',
            fields=[
                ('FlightNo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('AirlineCode', models.CharField(max_length=2)),
                ('DeptIATA', models.CharField(max_length=3)),
                ('ArrIATA', models.CharField(max_length=3)),
                ('DeptTime', models.CharField(max_length=20)),
                ('ArrTime', models.CharField(max_length=20)),
                ('Aircraft', models.CharField(max_length=15)),
                ('Distance', models.IntegerField()),
                ('OTD', models.CharField(max_length=5)),
                ('AvgDelay', models.IntegerField()),
                ('Monday', models.BooleanField(default=True)),
                ('Tuesday', models.BooleanField(default=True)),
                ('Wednesday', models.BooleanField(default=True)),
                ('Thursday', models.BooleanField(default=True)),
                ('Friday', models.BooleanField(default=True)),
                ('Saturday', models.BooleanField(default=True)),
                ('Sunday', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'djangoAirline',
            },
        ),
    ]
