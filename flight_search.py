import os
import requests
import json


class FlightSearch:
    """Manage search for flights
    
    Functionality:
        * Connect to API and search based on params given
        * Get IATA codes from flight API
        
    Attributes:
        kiwi_flight_search_endpoint: URL for flight search API
        kiwi_location_endpoint: URL for airport location API
        kiwi_headers: Headers passed to kiwi API in order to authenticate
    """

    def __init__(self) -> None:
        self.kiwi_flight_search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.kiwi_location_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.kiwi_headers = {
            "Content-Type": "application/json",
            "apikey": os.environ.get("KIWI_API_KEY"),
        }


    def search_for_flight(self, params:list) -> list:
        """Search for flights in kiwi API based on params given"""
        response = requests.get(url=self.kiwi_flight_search_endpoint, params=params, headers=self.kiwi_headers)

        with open("./hold_test_flight_data.json", "w") as datafile:
            json.dump(response.json(), datafile)

        return response.json()

    def get_iata_code(self, params:list) -> str:
        """Search kiwi API for IATA code based on destination name"""
        response = requests.get(url=self.kiwi_location_endpoint, params=params, headers=self.kiwi_headers)
        return response.json()["locations"][0]["code"]
