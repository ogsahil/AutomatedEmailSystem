import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
import os
import time

def load_template(template_file):
    env = Environment(loader=FileSystemLoader('.'))
    return env.get_template(template_file)

def send_email(smtp_server, smtp_port, smtp_user, smtp_pass, to_email, subject, template_vars):
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject

    body = template.render(template_vars)
    msg.attach(MIMEText(body, 'html'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
        print(f"Email successfully sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def main():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = os.getenv('SMTP_USER')
    smtp_pass = os.getenv('SMTP_PASS')

    global template
    template = load_template('template.html')

    # List of recipients with enhanced details
    recipients = [
        {'email': 'sahilnayak2056@gmail.com', 'name': 'Sahil Nayak', 'title': 'Welcome!', 'content': 'Thank you for joining us.'},
        {'email': 'contactsahilpnayak@gmail.com', 'name': 'Sahil P. Nayak', 'title': 'Hello!', 'content': 'Here is some important news.'},
        # Add more recipients here
    ]

    for recipient in recipients:
        subject = 'Demo for testing purpose - to check where its sending mails'
        template_vars = {
            'title': recipient['title'], 
            'content': recipient['content'],
            'name': recipient['name'],
            # Add more variables here if needed
        }
        send_email(smtp_server, smtp_port, smtp_user, smtp_pass, recipient['email'], subject, template_vars)

        # Rate limiting: Wait 2 seconds before sending the next email
        time.sleep(2)
    print("All the emails sent successfully to clients!")
if __name__ == '__main__':
    main()
