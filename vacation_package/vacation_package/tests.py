# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from vacation_package.VacationPackage import FlightReservation as fr
from vacation_package.VacationPackage import Flight as f
import datetime
# Create your tests here.

class TestVacationPackage(TestCase):
    def test_valid_inputs(self):
        flight = f("C", "D", datetime.date(2019, 4, 21),
                         datetime.date(2019, 4, 22), 200, 100)
        a = fr()
        print(a.bookFlight(2,4,flight))
        self.assertEqual("OK",a.bookFlight(2, 4, flight))

    def test_get_cost(self):
        flight = f("C", "D", datetime.date(2019, 4, 21),
                         datetime.date(2019, 4, 22), 200, 100)
        a = fr()
        print(a.bookFlight(2,4,flight))
        self.assertEqual("OK",a.bookFlight(2, 4, flight))
        self.assertEqual(800, a.getCost())

    def test_get_description(self):
        flight = f("C", "D", datetime.date(2019, 4, 21),
                         datetime.date(2019, 4, 22), 200, 100)
        a = fr()
        print(a.bookFlight(2,4,flight))
        self.assertEqual("OK",a.bookFlight(2, 4, flight))
        description = "Flight to D on 2019-04-21 for 2 adults and 4 children and back to C on 2019-04-22. Your ReservationID is: " + str(a.getreservationID())
        self.assertEqual(description, a.getDescription())

    def test_same_destination_error(self):
        flight = f("D", "D", datetime.date(2019, 4, 21),
                         datetime.date(2019, 4, 22), 200, 100)
        a = fr()
        print(a.bookFlight(2,4,flight))
        self.assertEqual("Source and Destination cannot be the same",a.bookFlight(2, 4, flight))


    def test_return_date_error(self):
        flight = f("C", "D", datetime.date(2019, 4, 21),
                         datetime.date(2019, 4, 21), 200, 100)
        a = fr()
        print(a.bookFlight(2,4,flight))
        self.assertEqual("Return date must be after flight arrival date at destination",a.bookFlight(2, 4, flight))


    def test_departure_date_error(self):
        flight = f("C", "D", datetime.date.today(),
                         datetime.date(2019, 4, 21), 200, 100)
        a = fr()
        print(a.bookFlight(2,4,flight))
        self.assertEqual("Departure date must atleast one day after date of reservation",a.bookFlight(2, 4, flight))


    def test_adult_error(self):
        flight = f("C", "D", datetime.date(2019, 4, 15),
                         datetime.date(2019, 4, 21), 200, 100)
        a = fr()
        print(a.bookFlight(0,4,flight))
        self.assertEqual("There has to be atleast one adult passenger",a.bookFlight(0, 4, flight))
