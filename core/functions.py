import os
import random
from twilio.rest import Client

from core.constants import SMS_BODY
from core.settings import PARTICIPANTS, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

def draw_names():
    names = list(PARTICIPANTS.keys())
    random.shuffle(names)

    results = {}
    for i in range(len(names)):
        results[names[i]] = names[(i+1) % len(names)]
    
    return results

def send_whatsapp(recipient_name, recipient_phone, secret_santa):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message_body = SMS_BODY.format(name=recipient_name, secret_santa=secret_santa)
    
    message = client.messages.create(
        body=message_body,
        from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
        to=f'whatsapp:{recipient_phone}'
    )

    print(f"WhatsApp message sent to {recipient_name} at {recipient_phone}")
