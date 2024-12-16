from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime, timedelta

def jeanLucDay(request, dt):
    # https: // en.wikipedia.org / wiki / Patrick_Stewart
    # Patrick Stewart born: July 13, 1940
    # https://en.wikipedia.org/wiki/Star_Trek:_The_Next_Generation
    # September 28, 1987
    #
    # 17,244 days
    #
    # Upcoming Celebrity:
    # https://en.wikipedia.org/wiki/Matt_Bomer

    d =  datetime.strptime(dt, '%Y-%m-%d').date()
    d = d + timedelta(days=17244)

    return render(request, 'core/jld.html', {'d': d, 'dt': dt})

def reverseJeanLucDay(request, dt):
    d =  datetime.strptime(dt, '%Y-%m-%d').date()
    d = d - timedelta(days=17244)

    return render(request, 'core/rjld.html', {'d': d, 'dt': dt})

def index(request):
    dt = date.today()
    birthday_dt = dt - timedelta(days=17244)

    return render(request, 'core/index.html', {'birthday_dt': birthday_dt, 'dt': dt})

