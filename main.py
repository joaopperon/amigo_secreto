from core.settings import PARTICIPANTS
from core.functions import draw_names, send_whatsapp

if __name__ == "__main__":
    result = draw_names()
    for name, secret_santa in result.items():
        phone = PARTICIPANTS[name]
        send_whatsapp(name, phone, secret_santa)
