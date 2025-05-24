import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert(subject, body, to_email):
    """Envía alertas por email."""
    msg = MIMEMultipart()
    msg["From"] = "auditoria@empresa.com"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("user", "password")
        server.send_message(msg)