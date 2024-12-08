# Projeto de Sorteio de Amigo Secreto

Este projeto realiza o sorteio de amigo secreto entre os participantes cadastrados e envia um e-mail para cada participante informando quem ele tirou. O projeto utiliza Python e bibliotecas como `smtplib` para envio de e-mails e `random` para realizar o sorteio.

## Estrutura do Projeto

- `functions.py`: Contém as funções principais para realizar o sorteio e enviar os e-mails.
- `settings.py`: Contém as configurações dos participantes e credenciais de e-mail.
- `constants.py`: Contém o modelo de mensagem em HTML para os e-mails.

## Configuração

1. Clone o repositório para sua máquina local.
2. Crie um ambiente virtual e instale as dependências necessárias.
3. Configure o arquivo `settings.py` com os participantes e as credenciais de e-mail.

### Exemplo de `settings.py`

```python
PARTICIPANTES = {
    'Alice': 'alice@example.com',
    'Bob': 'bob@example.com',
    'Charlie': 'charlie@example.com',
    # Adicione mais participantes aqui
}

EMAIL = 'seu_email@gmail.com'
SENHA_EMAIL = 'sua_senha'
EMAIL_MODE = 'PRODUCTION'  # Use 'DEBUG' para testes locais
EMAIL_SUBJECT = 'Amigo Secreto'
