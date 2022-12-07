from flight_search import FlightSearch
from datetime import datetime, timedelta

class FlightData:
    """Manage flight data
    
    Functionality:
        * Structure queries for flight API search
        * Check for cheapest flights


    Attributes:
        date_from: Date you are flying from
        date_to: Date you are flying till
        nights_in_dst_from: Min number of nights you plan on staying in your destination
        nights_in_dst_to: Max number of nights you plan on staying in your destination
        fly_from: Where you're flying from
        currency: Currency for prices returned from API
        max_layovers: Max number of layovers allowed to get to destination
    """
    
    def __init__(self) -> None:
        self.date_from = datetime.now() + timedelta(days=1)
        self.date_to = self.date_from + timedelta(days=60)
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 28
        self.fly_from = "NYC"
        self.currency = "USD"
        self.max_layovers = 1


    def create_flight_search_query(self, data:list) -> list:
        """Search for flights based on params provided"""
        flight_param_list = []
        for flight in data:
            params = {
                "date_from": self.date_from.strftime("%d/%m/%Y"),
                "date_to": self.date_to.strftime("%d/%m/%Y"),
                "nights_in_dst_from": self.nights_in_dst_from,
                "nights_in_dst_to": self.nights_in_dst_to,     
                "fly_from": self.fly_from,
                "fly_to": flight["iataCode"],
                "price_to": flight["lowestPrice"],
                "curr": self.currency,
                "max_stopover": self.max_layovers,
            }
            flight_param_list.append(params)

        return flight_param_list            

    def check_for_cheap_flights(self, flight_param_data:list) -> list:
        """From flights returned, get cheapest flight and condense down flight info to most important elements"""
        cheapest_flights = []
        for flight_params in flight_param_data:
            available_flights = FlightSearch().search_for_flight(flight_params)
            try:
                cheapest_flight_info = available_flights["data"][0]
                condensed_flight_info = {
                    "from_city": cheapest_flight_info["cityFrom"],
                    "to_city": cheapest_flight_info["cityTo"],
                    "fly_from": cheapest_flight_info["flyFrom"],
                    "fly_to": cheapest_flight_info["flyTo"],
                    "price": cheapest_flight_info["price"],
                    "depart_on": cheapest_flight_info["local_departure"][:17],
                    "arrive at": cheapest_flight_info["local_arrival"][:17],
                }
                cheapest_flights.append(condensed_flight_info) 
            except IndexError:
                continue   

        return cheapest_flights
