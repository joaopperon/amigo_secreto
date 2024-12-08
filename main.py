from core.settings import PARTICIPANTES
from core.functions import sortear_nomes, enviar_email

if __name__ == "__main__":
    resultado = sortear_nomes()
    for nome, amigo_secreto in resultado.items():
        email = PARTICIPANTES[nome]
        enviar_email(nome, email, amigo_secreto)
        print(f"Email enviado para {nome}!")