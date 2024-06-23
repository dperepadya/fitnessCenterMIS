import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from celery import Celery


app = Celery('celery_tasks', broker='pyamqp://guest@localhost//')


@app.task
def send_mail(recipient, subject, msg):
    try:
        # print(recipient, msg)
        port = 587
        smtp_server = 'smtp.gmail.com'
        sender_email = 'dperepadya@gmail.com'
        receiver_email = recipient
        password = os.environ.get('EMAIL_PASSWORD')
        # print(os.environ)
        # print(f"E-mail {recipient} Password: {password}")
        if password is None:
            print("EMAIL_PASSWORD environment variable is not set.")
            return False

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(msg, 'plain'))

        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        with smtplib.SMTP(host=smtp_server, port=port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email,  message.as_string())

        return True
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP authentication error: {e}")
    except Exception as e:
        print(f"Error sending email: {e}")
    return False
