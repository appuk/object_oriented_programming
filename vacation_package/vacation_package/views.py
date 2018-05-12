# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from vacation_package.VacationPackage import FlightReservation
from vacation_package.VacationPackage import Flight
import datetime

# Create your views here.


def index(request):
    a = FlightReservation()
    flight1 = Flight("C", "D", datetime.date(2019, 4, 21),
                     datetime.date(2019, 4, 22), 200, 100)
    flight2 = Flight("Clt", "Dallas", datetime.date(2019, 4, 21),
                     datetime.date(2019, 4, 22), 200, 100)
    status = a.bookFlight(2, 4, flight2)
    if status=="OK":
        return HttpResponse(a.getDescription())
    else:
        return HttpResponse(status)