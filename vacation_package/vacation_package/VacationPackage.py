from abc import ABCMeta, abstractmethod

import datetime


class IPackage(object):
    __metaclass__ = ABCMeta



class Flight:
	sourceLocation = ""
	Destination = ""
	departureDate = datetime.date.today()
	returnDate = datetime.date.today()
	costAdult = 0
	costChild = 0

	def __init__(self,
	             sourceLocation="NotGiven",
	             Destination="NotGiven",
	             departureDate=datetime.date.today(),
	             returnDate=datetime.date.today(),
	             costAdult=0,
	             costChild=0):
		self.setcostAdult(costAdult)
		self.setcostChild(costChild)
		self.setsourceLocation(sourceLocation)
		self.setDestination(Destination)
		self.setdepartureDate(departureDate)
		self.setreturnDate(returnDate)

	def getsourceLocation(self):
		return self.sourceLocation

	def setsourceLocation(self, location):
		self.sourceLocation = location

	def getDestination(self):
		return self.Destination

	def setDestination(self, location):
		self.Destination = location

	def getdepartureDate(self):
		return self.departureDate

	def setdepartureDate(self, departureDate):
		self.departureDate = departureDate

	def getreturnDate(self):
		return self.returnDate

	def setreturnDate(self, returnDate):
		self.returnDate = returnDate

	def getcostAdult(self):
		return self.costAdult

	def setcostAdult(self, costAdult):
		self.costAdult = costAdult

	def getcostChild(self):
		return self.costChild

	def setcostChild(self, costChild):
		self.costChild = costChild


class FlightReservation(IPackage):
	numberOfAdultPassengers = 0
	numberOfChildPassengers = 0
	reservationID = 0
	description = " "
	cost = 0.0
	flight = Flight()

	def getreservationID(self):
		return self.__class__.reservationID

	def getCost(self):
		return self.cost

	def setCost(self, cost):
		self.cost = cost

	def getDescription(self):
		return self.description

	def setDescription(self, description):
		self.description = description

	def getnumberOfAdultPassengers(self):
		return self.numberOfAdultPassengers

	def setnumberOfAdultPassengers(self, numberOfAdultPassengers):
		self.numberOfAdultPassengers = numberOfAdultPassengers

	def getnumberOfChildPassengers(self):
		return self.numberOfChildPassengers

	def setnumberOfChildPassengers(self, numberOfChildPassengers):
		self.numberOfChildPassengers = numberOfChildPassengers

	def validateFlightDetails(self, flight):
		if (flight.getsourceLocation() == flight.getDestination()):
			return "Source and Destination cannot be the same"
		if (flight.getdepartureDate() >= flight.getreturnDate()):
			return "Return date must be after flight arrival date at destination"
		if (flight.getdepartureDate() <= datetime.date.today()):
			return "Departure date must atleast one day after date of reservation"
		self.flight = flight
		return "OK"

	def bookFlight(self, numberOfAdultPassengers, numberOfChildPassengers,
	               flight):
		if (numberOfAdultPassengers == 0):
			return "There has to be atleast one adult passenger"
		self.setnumberOfChildPassengers(numberOfChildPassengers)
		self.setnumberOfAdultPassengers(numberOfAdultPassengers)
		status = self.validateFlightDetails(flight)
		if status == "OK":
			self.__class__.reservationID +=1
			description = "Flight to " + flight.getDestination(
			) + " on " + str(flight.getdepartureDate()) + " for " + str(
			    self.getnumberOfAdultPassengers()) + " adults and " + str(
			        self.getnumberOfChildPassengers()
			    ) + " children and back to " + flight.getsourceLocation(
			    ) + " on " + str(flight.getreturnDate()) + ". Your ReservationID is: " + str(self.getreservationID())
			self.setDescription(description)
			self.setCost(
			    (flight.getcostChild() * self.getnumberOfChildPassengers()) +
			    (flight.getcostAdult() * self.getnumberOfAdultPassengers()))
		return status