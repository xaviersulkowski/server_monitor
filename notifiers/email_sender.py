import smtplib
from settings import *


def send_email(emails_list, msg):
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.login(EMAIL_USER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, emails_list, msg)