import requests
API_KEY = input("Enter your Tequila API key: ")
TEQUILA_ENDPOINT_LOCATIONS = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_ENDPOINT_SEARCH = "https://tequila-api.kiwi.com/v2/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def find_codes(self, departure, destination):
        codes = []
        params = {
            "term": departure,
            "location-types": "city"
        }

        header = {
            "apikey": API_KEY
        }

        departRes = requests.get(url=TEQUILA_ENDPOINT_LOCATIONS, params=params, headers=header)
        departCode = departRes.json()["locations"][0]["code"]
        codes.append(departCode)

        params2 = {
            "term": destination,
            "location-types": "city"
        }

        destRes = requests.get(url=TEQUILA_ENDPOINT_LOCATIONS, params=params2, headers=header)
        destCode = destRes.json()["locations"][0]["code"]
        codes.append(destCode)

        return codes

    def find_flights(self, departCode, destCode, date_from, date_to):
        params = {
            "fly_from": departCode,
            "fly_to": destCode,
            "date_from": date_from,
            "date_to": date_to,
            "curr": "USD"
        }

        header = {
            "apikey": API_KEY
        }

        flights = requests.get(url=TEQUILA_ENDPOINT_SEARCH, params=params, headers=header)
        flights = flights.json()["data"][0]
        text = f"It only costs ${flights['price']} to travel from {flights['cityFrom']}-{flights['cityCodeFrom']} to {flights['cityTo']}-{flights['cityCodeTo']} from {date_from} to {date_to}"
        return text

