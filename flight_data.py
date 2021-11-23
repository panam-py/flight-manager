class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination

    def constructor(self):
        flightDic = {
            "Departure": self.departure,
            "Destination": self.destination,
        }
        return flightDic