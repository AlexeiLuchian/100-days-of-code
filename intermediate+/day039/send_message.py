import requests
import twilio.rest
from info import TWILIO_SID, TWILIO_TOKEN, tpn, pn


def send_message(message):
    client = twilio.rest.Client(TWILIO_SID, TWILIO_TOKEN)
    client.messages.create(body=message, from_=tpn, to=pn)
