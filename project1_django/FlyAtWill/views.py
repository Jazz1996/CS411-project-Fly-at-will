from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight, Airport
from datetime import datetime
from django.db.models import Q

# Create your views here.


def FlyAtWillPage(request):
    return render(request, 'FlyAtWill.html')


def SearchFlight(request):
    depart_airport = request.POST['From']
    arrival_airport = request.POST['To']

    # depart_date and return_date are string type.
    depart_date = request.POST['Depart']
    return_date = request.POST['Return']

    depart_day_tmp = datetime.strptime(depart_date, '%Y-%m-%d')
    depart_day = depart_day_tmp.weekday() + 1
    if return_date:
        return_day_tmp = datetime.strptime(return_date, '%Y-%m-%d')
        return_day = return_day_tmp.weekday() + 1

        if return_day == 1:
            return_result = Flight.objects.filter(Q(deptiata=arrival_airport) & Q(arriata=depart_airport) & Q(monday=1))
        elif return_day == 2:
            return_result = Flight.objects.filter(Q(deptiata=arrival_airport) & Q(arriate=depart_airport) & Q(tuesday=1))
        elif return_day == 3:
            return_result = Flight.objects.filter(Q(deptiata=arrival_airport) & Q(arriata=depart_airport) & Q(wednesday=1))
        elif return_day == 4:
            return_result = Flight.objects.filter(Q(deptiata=arrival_airport) & Q(arriata=depart_airport) & Q(thursday=1))
        elif return_day == 5:
            return_result = Flight.objects.filter(Q(deptiata=arrival_airport) & Q(arriata=depart_airport) & Q(friday=1))
        elif return_day == 6:
            return_result = Flight.objects.filter(Q(deptiata=arrival_airport) & Q(arriata=depart_airport) & Q(saturday=1))
        elif return_day == 7:
            return_result = Flight.objects.filter(Q(deptiata=arrival_airport) & Q(arriata=depart_airport) & Q(sunday=1))

    if depart_day == 1:
        one_way_result = Flight.objects.filter(Q(deptiata=depart_airport) & Q(arriata=arrival_airport) & Q(monday=1))
    elif depart_day == 2:
        one_way_result = Flight.objects.filter(Q(deptiata=depart_airport) & Q(arriata=arrival_airport) & Q(tuesday=1))
    elif depart_day == 3:
        one_way_result = Flight.objects.filter(Q(deptiata=depart_airport) & Q(arriata=arrival_airport) & Q(wednesday=1))
    elif depart_day == 4:
        one_way_result = Flight.objects.filter(Q(deptiata=depart_airport) & Q(arriata=arrival_airport) & Q(thursday=1))
    elif depart_day == 5:
        one_way_result = Flight.objects.filter(Q(deptiata=depart_airport) & Q(arriata=arrival_airport) & Q(friday=1))
    elif depart_day == 6:
        one_way_result = Flight.objects.filter(Q(deptiata=depart_airport) & Q(arriata=arrival_airport) & Q(saturday=1))
    elif depart_day == 7:
        one_way_result = Flight.objects.filter(Q(deptiata=depart_airport) & Q(arriata=arrival_airport) & Q(sunday=1))

    if return_date:
        return render(request, 'return_result.html', {'one_way_result': one_way_result, 'return_result': return_result})
    else:
        return render(request, 'one_way_result.html', {'one_way_result': one_way_result})


