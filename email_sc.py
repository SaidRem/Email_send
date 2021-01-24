import smtplib
from email.message import EmailMessage
from confidential import gmail_address, gmail_pas, ya_addr_1, ya_addr_2

EMAIL_AD = gmail_address
EMAIL_PAS = gmail_pas

def send_email(send_to=None):
    msg = EmailMessage()
    msg['Subject'] = 'This email has been sent through python script'
    msg['From'] = EMAIL_AD
    msg['To'] = send_to
    msg.set_content('Hello friend. My python script actually works')
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_AD, EMAIL_PAS)
        smtp.send_message(msg)


if __name__ == '__main__':
    send_email([gmail_address, ya_addr_2])