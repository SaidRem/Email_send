import smtplib
from email.message import EmailMessage
from confidential import gmail_address, gmail_password, yandex_address_1

EMAIL_AD = gmail_address
EMAIL_PAS = gmail_password

msg = EmailMessage()
msg['Subject'] = 'This email has been sent through python script'
msg['From'] = EMAIL_AD
msg['To'] = EMAIL_AD 
msg.set_content('Hello friend. My python script actually works')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_AD, EMAIL_PAS)
    smtp.send_message(msg)
