from apscheduler.schedulers.background import BackgroundScheduler
from models.user import get_all_users
from services.email_service import send_motivational_email
from app.config import Config
from datetime import datetime
import pytz  
import time
import os

def local_to_utc(hour, minute, local_tz="America/Bogota"):
    local_timezone = pytz.timezone(local_tz)
    utc_timezone = pytz.utc
    now_local = datetime.now(local_timezone)
    local_time = now_local.replace(hour=hour, minute=minute, second=0, microsecond=0)
    utc_time = local_time.astimezone(utc_timezone)
    return utc_time.hour, utc_time.minute

LOG_DIR = "/app/logs"
LOG_FILE = os.path.join(LOG_DIR, "email_log.txt")

os.makedirs(LOG_DIR, exist_ok=True)

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    with open(LOG_FILE, "a") as log_file:
        log_file.write(full_message + "\n")
    print(full_message)  

def send_motivational_email_with_retries(email, max_attempts=3, delay=60):
    attempts = 0
    while attempts < max_attempts:
        try:
            send_motivational_email(email)
            log_message(f"✅ Correo enviado a {email} en el intento {attempts + 1}")
            return
        except Exception as e:
            attempts += 1
            log_message(f"❌ Fallo al enviar a {email}. Intento {attempts}/{max_attempts}. Error: {e}")
            time.sleep(delay)
    log_message(f"⚠️ No se pudo enviar el correo a {email} tras {max_attempts} intentos.")  
   
def send_daily_motivational_emails():
    log_message("📩 Ejecutando envío de correos automáticos...")
    users = get_all_users()
    for user in users:
        send_motivational_email_with_retries(user['email'])

send_hour, send_minute = map(int, Config.SEND_TIME.split(':'))
utc_hour, utc_minute = local_to_utc(send_hour, send_minute)

scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_motivational_emails, 'cron', hour=utc_hour, minute=utc_minute)
scheduler.start()
