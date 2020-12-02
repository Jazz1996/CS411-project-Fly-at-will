from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight, Airport, FlyAtWill
from datetime import datetime
from django.db.models import Q
from django.db import connection, transaction

# Create your views here.


def FlyAtWillPage(request):
    return render(request, 'FlyAtWill.html')


def RecommendPage(request):
    return render(request, 'recommend.html')


def SearchFlight(request):
    depart_city = request.POST['From']
    arrival_city = request.POST['To']

    query_search = "SELECT f.flightno, f.airlinecode, dept.iatacode, arr.iatacode, f.depttime, f.arrtime \
                    FROM Flight f JOIN Airport dept ON f.deptiata=dept.iatacode \
                    JOIN Airport arr ON f.arriata=arr.iatacode \
                    WHERE dept.city = %s AND arr.city = %s"

    # depart_buf = Airport.objects.filter(city=depart_city)
    # arrival_buf = Airport.objects.filter(city=arrival_city)
    # depart_buf = Airport.objects.raw("SELECT * FROM Airport WHERE city = %s", [depart_city])
    # arrival_buf = Airport.objects.raw("SELECT * FROM Airport WHERE city = %s", [arrival_city])
    #
    # depart_airport_list = []
    # arrival_airport_list = []
    # for row in depart_buf:
    #     depart_airport_list.append(row.iatacode)
    # for row in arrival_buf:
    #     arrival_airport_list.append(row.iatacode)

    # depart_date and return_date are string type.
    depart_date = request.POST['Depart']
    return_date = request.POST['Return']

    depart_day_tmp = datetime.strptime(depart_date, '%Y-%m-%d')
    depart_day = depart_day_tmp.weekday() + 1

    cursor = connection.cursor()
    if return_date:
        return_day_tmp = datetime.strptime(return_date, '%Y-%m-%d')
        return_day = return_day_tmp.weekday() + 1
        return_result = Flight.objects.none()
        if return_day == 1:
            cursor.execute(query_search + " AND f.monday = 1", [arrival_city, depart_city])
            return_result = cursor.fetchall()
        elif return_day == 2:
            cursor.execute(query_search + " AND f.tuesday = 1", [arrival_city, depart_city])
            return_result = cursor.fetchall()
        elif return_day == 3:
            cursor.execute(query_search + " AND f.wednesday = 1", [arrival_city, depart_city])
            return_result = cursor.fetchall()
        elif return_day == 4:
            cursor.execute(query_search + " AND f.thursday = 1", [arrival_city, depart_city])
            return_result = cursor.fetchall()
        elif return_day == 5:
            cursor.execute(query_search + " AND f.friday = 1", [arrival_city, depart_city])
            return_result = cursor.fetchall()
        elif return_day == 6:
            cursor.execute(query_search + " AND f.saturday = 1", [arrival_city, depart_city])
            return_result = cursor.fetchall()
        elif return_day == 7:
            cursor.execute(query_search + " AND f.sunday = 1", [arrival_city, depart_city])
            return_result = cursor.fetchall()

    # if return_date:
    #     return_day_tmp = datetime.strptime(return_date, '%Y-%m-%d')
    #     return_day = return_day_tmp.weekday() + 1
    #
    #     return_result = Flight.objects.none()
    #     for arrival_airport in arrival_airport_list:
    #         for depart_airport in depart_airport_list:
    #             if return_day == 1:
    #                 return_result = return_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                     WHERE deptiata = %s AND arriata = %s AND monday=1", \
    #                                                     [arrival_airport, depart_airport]))
    #             elif return_day == 2:
    #                 return_result = return_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                     WHERE deptiata = %s AND arriata = %s AND tuesday=1", \
    #                                                    [arrival_airport, depart_airport]))
    #             elif return_day == 3:
    #                 return_result = return_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                     WHERE deptiata = %s AND arriata = %s AND wednesday=1", \
    #                                                    [arrival_airport, depart_airport]))
    #             elif return_day == 4:
    #                 return_result = return_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                     WHERE deptiata = %s AND arriata = %s AND thursday=1", \
    #                                                    [arrival_airport, depart_airport]))
    #             elif return_day == 5:
    #                 return_result = return_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                     WHERE deptiata = %s AND arriata = %s AND friday=1", \
    #                                                    [arrival_airport, depart_airport]))
    #             elif return_day == 6:
    #                 return_result = return_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                     WHERE deptiata = %s AND arriata = %s AND saturday=1", \
    #                                                    [arrival_airport, depart_airport]))
    #             elif return_day == 7:
    #                 return_result = return_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                     WHERE deptiata = %s AND arriata = %s AND sunday=1", \
    #                                                    [arrival_airport, depart_airport]))

    one_way_result = Flight.objects.none()
    if depart_day == 1:
        cursor.execute(query_search + " AND f.monday=1", [depart_city, arrival_city])
        one_way_result = cursor.fetchall()
    elif depart_day == 2:
        cursor.execute(query_search + " AND f.tuesday=1", [depart_city, arrival_city])
        one_way_result = cursor.fetchall()
    elif depart_day == 3:
        cursor.execute(query_search + " AND f.wednesday=1", [depart_city, arrival_city])
        one_way_result = cursor.fetchall()
    elif depart_day == 4:
        cursor.execute(query_search + " AND f.thursday=1", [depart_city, arrival_city])
        one_way_result = cursor.fetchall()
    elif depart_day == 5:
        cursor.execute(query_search + " AND f.friday=1", [depart_city, arrival_city])
        one_way_result = cursor.fetchall()
    elif depart_day == 6:
        cursor.execute(query_search + " AND f.saturday=1", [depart_city, arrival_city])
        one_way_result = cursor.fetchall()
    elif depart_day == 7:
        cursor.execute(query_search + " AND f.sunday=1", [depart_city, arrival_city])
        one_way_result = cursor.fetchall()

    # for arrival_airport in arrival_airport_list:
    #     for depart_airport in depart_airport_list:
    #         if depart_day == 1:
    #             # tmp = Flight.objects.filter(Q(deptiata=depart_airport) & Q(arriata=arrival_airport) & Q(monday=1))
    #             # one_way_result = one_way_result | tmp
    #             # cursor.execute("SELECT flightno, airlinecode, deptiata, arriata, depttime, arrtime \
    #             #                 FROM Flight \
    #             #                 WHERE deptiata = depart_airport AND arriata = arrival_airport AND monday=1")
    #             # one_way_result = cursor.fetchall()
    #             one_way_result = Flight.objects.raw("SELECT * FROM Flight \
    #                                                 WHERE deptiata = %s AND arriata = %s AND monday=1", \
    #                                                 [depart_airport, arrival_airport])
    #         elif depart_day == 2:
    #             one_way_result = one_way_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                 WHERE deptiata = %s AND arriata = %s AND tuesday=1", \
    #                                                 [depart_airport, arrival_airport]))
    #         elif depart_day == 3:
    #             one_way_result = one_way_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                 WHERE deptiata = %s AND arriata = %s AND wednesday=1", \
    #                                                 [depart_airport, arrival_airport]))
    #         elif depart_day == 4:
    #             one_way_result = one_way_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                 WHERE deptiata = %s AND arriata = %s AND thursday=1", \
    #                                                 [depart_airport, arrival_airport]))
    #         elif depart_day == 5:
    #             one_way_result = one_way_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                 WHERE deptiata = %s AND arriata = %s AND friday=1", \
    #                                                 [depart_airport, arrival_airport]))
    #         elif depart_day == 6:
    #             one_way_result = one_way_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                 WHERE deptiata = %s AND arriata = %s AND saturday=1", \
    #                                                 [depart_airport, arrival_airport]))
    #         elif depart_day == 7:
    #             one_way_result = one_way_result.union(Flight.objects.raw("SELECT * FROM Flight \
    #                                                 WHERE deptiata = %s AND arriata = %s AND sunday=1", \
    #                                                 [depart_airport, arrival_airport]))

    if return_date:
        return render(request, 'return_result.html', {'one_way_result': one_way_result, 'return_result': return_result})
    else:
        return render(request, 'one_way_result.html', {'one_way_result': one_way_result})

    # feature_list = SentenceProcess(request.POST['To'])


def SentenceProcess(sentence):
    low_weight = 0.1
    high_weight = 10
    background_vocalbulary = ["I", "want", "to", "go", "a", "the", "an", "place", "with", "of", "A", "that", "has", ",",\
                              "and", "city", "food"]
    word_list = sentence.split()
    sen_dict = {}
    for word in word_list:
        if word in background_vocalbulary:
            sen_dict[word] = low_weight
        else:
            sen_dict[word] = high_weight
    output = []
    for key in sen_dict:
        if sen_dict[key] != low_weight and len(output) < 5:
            output.append(key)
    return output


def RecommendFlight(request):
    depart_city = request.POST['From']
    user_preference = request.POST['Preference']
    feature_list = SentenceProcess(user_preference)
    recommend_results = FlyAtWill.objects.all()
    for feature in feature_list:
        recommend_results = recommend_results.filter(characteristics__icontains=feature)

    arrival_city = {}
    for row in recommend_results:
        if row.cityName != depart_city:
            arrival_city[row.cityName] = row.description

    recommend_flights = []
    to_be_del_keys = []
    for key in arrival_city:
        query_search = "SELECT f.flightno, f.airlinecode, dept.iatacode, arr.iatacode, f.depttime, f.arrtime, f.monday, f.tuesday, f.wednesday, f.thursday, f.friday, f.saturday, f.sunday \
                        FROM Flight f JOIN Airport dept ON f.deptiata=dept.iatacode \
                        JOIN Airport arr ON f.arriata=arr.iatacode \
                        WHERE dept.city = %s AND arr.city = %s"
        cursor = connection.cursor()
        cursor.execute(query_search, [depart_city, key])
        tmp_result = cursor.fetchall()
        if tmp_result:
            recommend_flights.append(tmp_result)
        else:
            to_be_del_keys.append(key)
    for key in to_be_del_keys:
        del arrival_city[key]

    return render(request, 'recommend_result.html', {'arrival_city': arrival_city, 'recommend_flights': recommend_flights})


def search(request):
    # return HttpResponse('<input type="text" />')
    return render(request, 'search.html')


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
                            Saturday=%s, Sunday=%s WHERE FlightNo=%s",[airlinecode,deptiata,arriata,depttime,arrtime,\
                            aircraft,int(distance),otd,int(avgdelay),bool(monday),bool(tuesday),bool(wednesday),\
                                            bool(thursday),bool(friday),bool(saturday),bool(sunday),flightno])
                transaction.commit()
            return render(request, 'manage.html', {'msg': 'Record has been successfully updated!'})
        else:
            return render(request, 'update.html', {'f': flight_up, 'msg': 'Invalid input!'})
