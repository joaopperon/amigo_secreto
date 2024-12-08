EMAIL_BODY = """
<!DOCTYPE html>
<html>
<head>
    <title>Amigo Secreto</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            padding: 20px;
        }}
        .container {{
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .footer {{
            text-align: center;
            margin-top: 20px;
            font-size: 12px;
            color: #777;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Amigo Secreto</h1>
        </div>
        <p>Olá, {nome}!</p>
        <p>Você tirou <strong>{amigo_secreto}</strong> no amigo secreto!</p>
        <p>Boa sorte e divirta-se!</p>
        <div class="footer">
            <p>Este é um e-mail automático, por favor, não responda.</p>
        </div>
    </div>
</body>
</html>
"""