"""cs411 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.shortcuts import HttpResponse,render
from second.models import djangoAirline
import datetime


def search(request):
    # return HttpResponse('<input type="text" />')
    return render(request,'search.html')


def search_result(request):
    sr = {}
    print('DeptIATA: ', request.POST.get('dept'))
    dept = request.POST.get('dept')
    print('ArrIATA: ', request.POST.get('arr'))
    arr = request.POST.get('arr')
    print('Date: ', request.POST.get('date'))
    if len(dept)>0 and len(arr)>0:
        sr = djangoAirline.objects.filter(DeptIATA=dept,ArrIATA=arr)
    elif len(dept)>0:
        sr = djangoAirline.objects.filter(DeptIATA=dept)
    elif len(arr)>0:
        sr = djangoAirline.objects.filter(ArrIATA=arr)
    else:
        return render(request,'search_result.html',{'msg': 'Invalid input! Please check!'})
    if sr.exists():
        return render(request,'search_result.html',{'msg': 'Result is listed below', 'sr': sr})
    else:
        return render(request,'search_result.html',{'msg': 'No records found!'})


def manage(request):
    sr = {}
    filter_num = 0

    if request.method == "GET":
        return render(request, 'manage.html')
    flightno = request.POST.get('flightno')
    airlinecode = request.POST.get('airlinecode')
    deptiata = request.POST.get('deptiata')
    arriata = request.POST.get('arriata')
    depttime = request.POST.get('depttime')
    arrtime = request.POST.get('arrtime')
    aircraft = request.POST.get('aircraft')
    distance = request.POST.get('distance')
    otd = request.POST.get('otd')
    avgdelay = request.POST.get('avgdelay')
    monday = request.POST.get('monday')
    tuesday = request.POST.get('tuesday')
    wednesday= request.POST.get('wednesday')
    thursday= request.POST.get('thursday')
    friday = request.POST.get('friday')
    saturday = request.POST.get('saturday')
    sunday= request.POST.get('sunday')
    sr = djangoAirline.objects.filter()
    if flightno == '*':
        return render(request, 'manage.html', {'msg': 'Got the records!', 'sr': sr})
    if flightno!='':
        sr = sr.filter(FlightNo=flightno)
        filter_num+=1
    if airlinecode!='':
        sr = sr.filter(AirlineCode=airlinecode)
        filter_num += 1
    if deptiata!='':
        sr = sr.filter(DeptIATA=deptiata)
        filter_num += 1
    if arriata!='':
        sr = sr.filter(ArrIATA=arriata)
        filter_num += 1
    if depttime!='':
        depttime_sql = datetime.datetime.strptime(depttime,'%H:%M')
        sr = sr.filter(DeptTime=depttime_sql)
        filter_num += 1
    if arrtime!='':
        arrtime_sql = datetime.datetime.strptime(arrtime,'%H:%M')
        sr = sr.filter(ArrTime=arrtime_sql)
        filter_num += 1
    if aircraft!='':
        sr = sr.filter(Aircraft=aircraft)
        filter_num += 1
    if distance!='':
        sr = sr.filter(Distance=distance)
        filter_num += 1
    if otd!='':
        sr = sr.filter(OTD=otd)
        filter_num += 1
    if avgdelay!='':
        sr = sr.filter(AvgDelay=avgdelay)
        filter_num += 1
    if monday!='':
        sr = sr.filter(Monday=monday)
        filter_num += 1
    if tuesday!='':
        sr = sr.filter(Tuesday=tuesday)
        filter_num += 1
    if wednesday!='':
        sr = sr.filter(Wednesday=wednesday)
        filter_num += 1
    if thursday!='':
        sr = sr.filter(Thursday=thursday)
        filter_num += 1
    if friday!='':
        sr = sr.filter(Friday=friday)
        filter_num += 1
    if saturday!='':
        sr = sr.filter(Saturday=saturday)
        filter_num += 1
    if sunday!='':
        sr = sr.filter(Sunday=sunday)
        filter_num += 1
    if sr.exists() and filter_num!= 0:
        return render(request, 'manage.html', {'msg': 'Got the records!', 'sr': sr})
    else:
        return render(request, 'manage.html', {'msg': 'No records found'})


def delete(request):
    flightno_del = request.GET.get('nid')
    flight = djangoAirline.objects.get(FlightNo=flightno_del)
    flight.delete()
    return render(request, 'manage.html', {'msg': 'Delete succeed!'})


def insert(request):
    if request.method == "GET":
        return render(request, 'insert.html')
    else:
        flight = djangoAirline()
        flightno = request.POST.get('flightno')
        airlinecode = request.POST.get('airlinecode')
        deptiata = request.POST.get('deptiata')
        arriata = request.POST.get('arriata')
        depttime_s = request.POST.get('depttime')
        arrtime_s = request.POST.get('arrtime')
        aircraft = request.POST.get('aircraft')
        distance = request.POST.get('distance')
        otd = request.POST.get('otd')
        avgdelay = request.POST.get('avgdelay')
        monday = request.POST.get('monday')
        tuesday = request.POST.get('tuesday')
        wednesday = request.POST.get('wednesday')
        thursday = request.POST.get('thursday')
        friday = request.POST.get('friday')
        saturday = request.POST.get('saturday')
        sunday = request.POST.get('sunday')
        if flightno!='' and airlinecode!='' and deptiata!='' and arriata!='' and \
                depttime_s!='' and arrtime_s!='' and aircraft!='' and distance!='' and \
                otd!='' and avgdelay!='' and monday!='' and tuesday!='' and \
                wednesday!='' and thursday!='' and friday!='' and saturday!='' and \
                sunday!='':
            flight.FlightNo = flightno
            flight.AirlineCode = airlinecode
            flight.DeptIATA = deptiata
            flight.ArrIATA = arriata
            depttime = datetime.datetime.strptime(depttime_s, '%H:%M')
            flight.DeptTime = depttime
            arrtime = datetime.datetime.strptime(arrtime_s, '%H:%M')
            flight.ArrTime = arrtime
            flight.Aircraft = aircraft
            flight.Distance = int(distance)
            flight.OTD = otd
            flight.AvgDelay = int(avgdelay)
            flight.Monday = bool(monday)
            flight.Tuesday = bool(tuesday)
            flight.Wednesday = bool(wednesday)
            flight.Thursday = bool(thursday)
            flight.Friday = bool(friday)
            flight.Saturday = bool(saturday)
            flight.Sunday = bool(sunday)
            flight.save()
            return render(request, 'insert.html',{'msg': 'Record has been successfully inserted!'})
        else:
            return render(request, 'insert.html',{'msg': 'Invalid inputs! Please check!'})


def update(request):
    flight_up = {}
    if request.method == "GET":
        flightno_up = request.GET.get('nid')
        flight_up = djangoAirline.objects.filter(FlightNo=flightno_up)
        return render(request, 'update.html', {'f': flight_up})
    else:
        flightno = request.POST.get('flightno')
        airlinecode = request.POST.get('airlinecode')
        deptiata = request.POST.get('deptiata')
        arriata = request.POST.get('arriata')
        depttime_s = request.POST.get('depttime')
        arrtime_s = request.POST.get('arrtime')
        aircraft = request.POST.get('aircraft')
        distance = request.POST.get('distance')
        otd = request.POST.get('otd')
        avgdelay = request.POST.get('avgdelay')
        monday = request.POST.get('monday')
        tuesday = request.POST.get('tuesday')
        wednesday = request.POST.get('wednesday')
        thursday = request.POST.get('thursday')
        friday = request.POST.get('friday')
        saturday = request.POST.get('saturday')
        sunday = request.POST.get('sunday')
        if flightno != '' and airlinecode != '' and deptiata != '' and arriata != '' and \
                depttime_s != '' and arrtime_s != '' and aircraft != '' and distance != '' and \
                otd != '' and avgdelay != '' and monday != '' and tuesday != '' and \
                wednesday != '' and thursday != '' and friday != '' and saturday != '' and \
                sunday != '':
            flight = djangoAirline.objects.get(FlightNo=flightno)
            flight.FlightNo = flightno
            flight.AirlineCode = airlinecode
            flight.DeptIATA = deptiata
            flight.ArrIATA = arriata
            depttime = datetime.datetime.strptime(depttime_s, '%H:%M')
            flight.DeptTime = depttime
            arrtime = datetime.datetime.strptime(arrtime_s, '%H:%M')
            flight.ArrTime = arrtime
            flight.Aircraft = aircraft
            flight.Distance = int(distance)
            flight.OTD = otd
            flight.AvgDelay = int(avgdelay)
            flight.Monday = bool(monday)
            flight.Tuesday = bool(tuesday)
            flight.Wednesday = bool(wednesday)
            flight.Thursday = bool(thursday)
            flight.Friday = bool(friday)
            flight.Saturday = bool(saturday)
            flight.Sunday = bool(sunday)
            flight.save()
            return render(request, 'manage.html', {'msg': 'Record has been successfully updated!'})
        else:
            return render(request, 'update.html', {'f': flight_up, 'msg': 'Invalid input!'})



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('search/', search),
    path('search/result', search_result),
    path('manage/', manage),
    path('manage/delete/', delete),
    path('manage/insert/', insert),
    path('manage/update/', update)
]
