# Generated by Django 3.1.3 on 2020-11-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('deptcity', models.CharField(blank=True, db_column='DeptCity', max_length=20, null=True)),
                ('arrcity', models.CharField(blank=True, db_column='ArrCity', max_length=20, null=True)),
                ('numbers', models.CharField(db_column='Numbers', max_length=10, primary_key=True, serialize=False)),
                ('airlines', models.CharField(blank=True, db_column='Airlines', max_length=5, null=True)),
                ('flightdate', models.DateField(blank=True, db_column='FlightDate', null=True)),
                ('depttime', models.TimeField(blank=True, db_column='DeptTime', null=True)),
                ('arrtime', models.TimeField(blank=True, db_column='ArrTime', null=True)),
                ('deptiata', models.CharField(blank=True, db_column='DeptIATA', max_length=3, null=True)),
                ('arriata', models.CharField(blank=True, db_column='ArrIATA', max_length=3, null=True)),
            ],
            options={
                'db_table': 'Flight',
                'managed': False,
            },
        ),
    ]
