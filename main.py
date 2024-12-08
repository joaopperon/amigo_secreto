from core.settings import PARTICIPANTS
from core.functions import draw_names, send_mail

if __name__ == "__main__":
    result = draw_names()
    for name, secret_santa in result.items():
        email = PARTICIPANTS[name]
        send_mail(name, email, secret_santa)
        print(f"Email enviado para {name}!")