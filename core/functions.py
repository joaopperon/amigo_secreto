import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from core.constants import EMAIL_BODY
from core.settings import (
    PARTICIPANTS, 
    SENDER_EMAIL, 
    SENDER_EMAIL_PASSWORD, 
    EMAIL_MODE, 
    EMAIL_SUBJECT, 
    EMAIL_HOST, 
    EMAIL_PORT
)

def draw_names():
    names = list(PARTICIPANTS.keys())
    random.shuffle(names)

    results = {}
    for i in range(len(names)):
        results[names[i]] = names[(i+1) % len(names)]
    
    return results

def send_mail(recipient_name, recipient_mail, secret_santa):
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = recipient_mail
    message['Subject'] = EMAIL_SUBJECT
    message.attach(MIMEText(EMAIL_BODY.format(nome=recipient_name, amigo_secreto=secret_santa), 'html'))

    try:
        if EMAIL_MODE == "DEBUG":
            with smtplib.SMTP('localhost', 1025) as server:
                server.sendmail(SENDER_EMAIL, recipient_mail, message.as_string())
                server.quit()
        else:
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.ehlo()
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_EMAIL_PASSWORD)
                server.sendmail(SENDER_EMAIL, recipient_mail, message.as_string())
                server.quit()
    except Exception as e:
        print(f"Erro ao enviar email para {recipient_name}: {e}")