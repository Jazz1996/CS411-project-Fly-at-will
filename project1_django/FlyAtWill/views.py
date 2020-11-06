from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight


# Create your views here.


def FlyAtWillPage(request):
    return render(request, 'FlyAtWill.html')


def SearchFlight(request):
    depart_airport = request.POST['From']
    arrival_airport = request.POST['To']
    depart_date = request.POST['Depart']
    return_date = request.POST['Return']
    result = Flight.objects.filter(deptiata=depart_airport)
    return render(request, 'result.html', {'result': result})
