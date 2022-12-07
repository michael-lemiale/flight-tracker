from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    # Set up data management for google sheets with destinations and flights
    data = DataManager().read_google_sheet_data()
    formatted_flight_data = FlightData().create_flight_search_query(data)
    cheapest_flights = FlightData().check_for_cheap_flights(formatted_flight_data)
    
    # If flights are found, send message
    if cheapest_flights:
        for flight in cheapest_flights:
            msg = (
                f"Cheap flight alert.\n"
                f"Fly to {flight['to_city']}-{flight['fly_to']} from {flight['from_city']}-{flight['fly_from']} "
                f"for only ${flight['price']}."
            )
            NotificationManager().send_message(msg)
