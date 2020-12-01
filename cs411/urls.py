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
from second.models import Flight
from django.db import connection,transaction
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
    query_sent = "SELECT * FROM Flight"
    if len(dept)>0 and len(arr)>0:
        # sr = Flight.objects.raw("SELECT * FROM Flight WHERE DeptIATA=%s and ArrIATA=%s",[dept, arr])
        query_sent = query_sent + " WHERE DeptIATA='%s' AND ArrIATA='%s'" % (dept,arr)
        sr = Flight.objects.raw(query_sent)
    elif len(dept)>0:
        query_sent = query_sent + " WHERE DeptIATA='%s'" % dept
        sr = Flight.objects.raw(query_sent)
    elif len(arr)>0:
        query_sent = query_sent + " WHERE ArrIATA='%s'" % arr
        sr = Flight.objects.raw(query_sent)
    else:
        return render(request,'search_result.html',{'msg': 'Invalid input! Please check!'})
    if sum(1 for tmp in sr) > 0:
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
    query_sent = "SELECT * FROM Flight WHERE 1=1"
    if flightno == '*':
        sr = Flight.objects.raw(query_sent)
        return render(request, 'manage.html', {'msg': 'Got the records!', 'sr': sr})
    if flightno!='':
        query_sent = query_sent + " AND FlightNo='%s'" %flightno
        filter_num+=1
    if airlinecode!='':
        query_sent = query_sent + " AND AirlineCode='%s'" %airlinecode
        filter_num += 1
    if deptiata!='':
        query_sent = query_sent + " AND DeptIATA='%s'" %deptiata
        filter_num += 1
    if arriata!='':
        query_sent = query_sent + " AND ArrIATA='%s'" %arriata
        filter_num += 1
    if depttime!='':
        depttime_sql = datetime.datetime.strptime(depttime,'%H:%M')
        query_sent = query_sent + " AND DeptTime='%s'" %depttime_sql
        filter_num += 1
    if arrtime!='':
        arrtime_sql = datetime.datetime.strptime(arrtime,'%H:%M')
        query_sent = query_sent + " AND ArrTime='%s'" %arrtime_sql
        filter_num += 1
    if aircraft!='':
        query_sent = query_sent + " AND Aircraft='%s'" %aircraft
        filter_num += 1
    if distance!='':
        query_sent = query_sent + " AND Distance=%s" %distance
        filter_num += 1
    if otd!='':
        query_sent = query_sent + " AND OTD='%s'" %otd
        filter_num += 1
    if avgdelay!='':
        query_sent = query_sent + " AND AvgDelay=%s" %avgdelay
        filter_num += 1
    if monday!='':
        query_sent = query_sent + " AND Monday=%s" %monday
        filter_num += 1
    if tuesday!='':
        query_sent = query_sent + " AND Tuesday=%s" %tuesday
        filter_num += 1
    if wednesday!='':
        query_sent = query_sent + " AND Wednesday=%s" %wednesday
        filter_num += 1
    if thursday!='':
        query_sent = query_sent + " AND Thursday=%s" %thursday
        filter_num += 1
    if friday!='':
        query_sent = query_sent + " AND Friday=%s" %friday
        filter_num += 1
    if saturday!='':
        query_sent = query_sent + " AND Saturday=%s" %saturday
        filter_num += 1
    if sunday!='':
        query_sent = query_sent + " AND Sunday=%s" %sunday
        filter_num += 1
    sr = Flight.objects.raw(query_sent)
    if sum(1 for tmp in sr)>0 and filter_num!= 0:
        return render(request, 'manage.html', {'msg': 'Got the records!', 'sr': sr})
    else:
        return render(request, 'manage.html', {'msg': 'No records found'})


def delete(request):
    flightno_del = request.GET.get('nid')
    with connection.cursor() as cur:
        cur.execute("DELETE FROM Flight WHERE FlightNo=%s",[flightno_del])
        transaction.commit()
    return render(request, 'manage.html', {'msg': 'Delete succeed!'})


def insert(request):
    if request.method == "GET":
        return render(request, 'insert.html')
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
        if flightno!='' and airlinecode!='' and deptiata!='' and arriata!='' and \
                depttime_s!='' and arrtime_s!='' and aircraft!='' and distance!='' and \
                otd!='' and avgdelay!='' and monday!='' and tuesday!='' and \
                wednesday!='' and thursday!='' and friday!='' and saturday!='' and \
                sunday!='':
            depttime = datetime.datetime.strptime(depttime_s, '%H:%M')
            arrtime = datetime.datetime.strptime(arrtime_s, '%H:%M')
            with connection.cursor() as cur:
                cur.execute("INSERT INTO Flight VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[flightno,airlinecode,deptiata,arriata,depttime,arrtime,aircraft,int(distance),otd,int(avgdelay),bool(monday),bool(tuesday),bool(wednesday),bool(thursday),bool(friday),bool(saturday),bool(sunday)])
                transaction.commit()
            return render(request, 'insert.html',{'msg': 'Record has been successfully inserted!'})
        else:
            return render(request, 'insert.html',{'msg': 'Invalid inputs! Please check!'})


def update(request):
    flight_up = {}
    if request.method == "GET":
        flightno_up = request.GET.get('nid')
        flight_up = Flight.objects.raw("SELECT * FROM Flight WHERE FlightNo=%s",[flightno_up])
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
            depttime = datetime.datetime.strptime(depttime_s, '%H:%M')
            arrtime = datetime.datetime.strptime(arrtime_s, '%H:%M')
            #insrow = "UPDATE Flight SET"
            #insrow = insrow + " AirlineCode='%s'" %airlinecode
            #insrow = insrow + " DeptIATA='%s'" % deptiata
            with connection.cursor() as cur:
                cur.execute("UPDATE Flight SET AirlineCode=%s, DeptIATA=%s, \
                            ArrIATA=%s, DeptTime=%s, ArrTime=%s, \
                            Aircraft=%s, Distance=%s, OTD=%s, \
                            AvgDelay=%s, Monday=%s, Tuesday=%s, \
                            Wednesday=%s, Thursday=%s, Friday=%s, \
                            Saturday=%s, Sunday=%s WHERE FlightNo=%s",[airlinecode,deptiata,arriata,depttime,arrtime,aircraft,int(distance),otd,int(avgdelay),bool(monday),bool(tuesday),bool(wednesday),bool(thursday),bool(friday),bool(saturday),bool(sunday),flightno])
                transaction.commit()
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
    path('manage/update/', update),
]
