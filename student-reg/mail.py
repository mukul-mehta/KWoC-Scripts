import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(to_mail, subject, body):
    message = Mail(
    from_email='admin@kossiitkgp.org',
    to_emails=to_mail,
    subject=subject,
    html_content=body)
    
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)