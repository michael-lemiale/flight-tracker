import requests
import os
import json

from flight_search import FlightSearch


class DataManager:
    """Manage data in google sheet
    
    Functionality:
        * Update google sheet rows
        * Read in google sheet data
    
    Attributes:
        sheety_endpoint: API URL for google sheet manager
        sheety_headers: Header params for Sheety API
    """
    
    def __init__(self) -> None:
        self.sheety_endpoint = "https://api.sheety.co/a4eff1476bb629e7081dc4c7c5a68ee8/flightDeals/prices"
        self.sheety_headers = {
            "Authorization": os.environ.get("SHEETY_AUTH_KEY"),
            "Content-Type": "application/json",
        }


    def update_google_sheet_rows(self, rows:list) -> None:
        """Update google sheet with IATA codes for cities"""
        for row in rows:
            search_params = {
                "term": row['city'],
                "locale": "en-US",
                "location_types": "city",
                "limit": 1,
            }

            update_data = {
                "price": {
                    "iataCode": FlightSearch().get_iata_code(search_params)
                }
            }
            update_data = json.dumps(update_data)
            
            response = requests.put(url=f"{self.sheety_endpoint}/{row['id']}", data=update_data, headers=self.sheety_headers)
            response.raise_for_status()

    def read_google_sheet_data(self) -> list:
        """Read google sheet data and return as dict"""
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        data = response.json()["prices"]
        return data
