import os

from twilio.rest import Client


class NotificationManager:
    """Manage sending notifications when flight is cheap
    
    Functionality:
        * Send message to phone
        
    Attributes:
        twilio_api_key: API key to auth into Twilio
        twilio_account_id: Account ID to auth into Twilio
        send_from: Twilio account number used to send messages
        send_to: Number to send messages about cheap flights
    """
    def __init__(self) -> None:
        self.twilio_api_key = os.environ.get("TWILIO_API_KEY")
        self.twilio_account_id = os.environ.get("TWILIO_ACCOUNT_ID")
        self.send_from = os.environ.get("SEND_FROM_NUMBER")
        self.send_to = os.environ.get("SEND_TO_NUMBER")


    def send_message(self, msg) -> None:
        """Send message through Twilio about cheap flights"""
        client = Client(self.twilio_account_id, self.twilio_api_key)
        msg_body = f"{msg}" 
        message = client.messages.create(
                body=msg_body,
                from_=self.send_from,
                to=self.send_to,
        )
        print(message.sid)
