from celery import Celery

app = Celery('celery_tasks', broker='pyamqp://guest@localhost//')


@app.task
def send_mail(recipient, msg):
    print(recipient, msg)
    '''
    port = 587
    smtp_server = 'smtp.gmail.com'
    sender_email = 'dperepadya@gmail.com'
    receiver_email = recipient
    password = ''
    message = MIMEText(msg, 'plain', 'utf-8')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)
        # server.quit()
    '''
    return True
