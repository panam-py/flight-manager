#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import timedelta, date
from flight_data import FlightData
from flight_search import FlightSearch

departure = input("What city will you be departing from: ")
destination = input("What city is your destination: ")

newFlight = FlightData(departure, destination)
newFlightDets = newFlight.constructor()

newSearch = FlightSearch()
codes = newSearch.find_codes(newFlightDets["Departure"], newFlightDets["Destination"])

today = date.today()
tommorow = today + timedelta(days=1)
nextSixMonths = tommorow + timedelta(days=6*30)
tommorow = tommorow.strftime("%d/%m/%Y")
nextSixMonths = nextSixMonths.strftime("%d/%m/%Y")

result = newSearch.find_flights(codes[0], codes[1], tommorow, nextSixMonths)
print(result)


