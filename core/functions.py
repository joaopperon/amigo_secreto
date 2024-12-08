import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from core.constants import EMAIL_BODY
from core.settings import PARTICIPANTES, EMAIL, SENHA_EMAIL, EMAIL_MODE, EMAIL_SUBJECT

def sortear_nomes():
    nomes = list(PARTICIPANTES.keys())
    random.shuffle(nomes)

    resultado = {}
    for i in range(len(nomes)):
        resultado[nomes[i]] = nomes[(i+1) % len(nomes)]
    
    return resultado

def enviar_email(nome_destinatario, email_destinatario, nome_amigo_secreto):
    mensagem = MIMEMultipart()
    mensagem['From'] = EMAIL
    mensagem['To'] = email_destinatario
    mensagem['Subject'] = EMAIL_SUBJECT
    mensagem.attach(MIMEText(EMAIL_BODY.format(nome=nome_destinatario, amigo_secreto=nome_amigo_secreto), 'html'))

    try:
        if EMAIL_MODE == "DEBUG":
            with smtplib.SMTP('localhost', 1025) as server:
                server.sendmail(EMAIL, email_destinatario, mensagem.as_string())
                server.quit()
        else:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(EMAIL, SENHA_EMAIL)
                server.sendmail(EMAIL, email_destinatario, mensagem.as_string())
                server.quit()
    except Exception as e:
        print(f"Erro ao enviar email para {nome_destinatario}: {e}")