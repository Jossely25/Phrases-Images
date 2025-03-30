import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from app.config import Config
from services.phrase_service import chat_with_gemini  
from services.image_service import get_image_from_pexels
import requests
from io import BytesIO
import random

def send_motivational_email(to):
    quote = chat_with_gemini() 

    image_url = get_image_from_pexels("motivational")
    
    response = requests.get(image_url)
    img_data = BytesIO(response.content)

    subject = "Tu mensaje motivacional del día"
    body = f"""
    ¡Hola!

    Aquí tienes tu frase motivacional del día:

    "{quote}"

    Y una imagen inspiradora para que sigas adelante:
    <img src="cid:image1" alt="Imagen motivacional" style="width:100%; border-radius: 10px;"/>

    ¡Que tengas un excelente día!
    """

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    server.login(Config.GMAIL_USER, Config.GMAIL_PASS)

    msg = MIMEMultipart()
    msg['From'] = Config.GMAIL_USER
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    image = MIMEImage(img_data.read())
    image.add_header('Content-ID', '<image1>')  
    msg.attach(image)

    server.sendmail(Config.GMAIL_USER, to, msg.as_string())
    server.quit()

    print(f"Correo enviado a {to}")
    