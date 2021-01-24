import smtplib
from email.message import EmailMessage
from confidential import gmail_address, gmail_pas, ya_addr_1, ya_addr_2, file_math_py

EMAIL_AD = gmail_address
EMAIL_PAS = gmail_pas

def send_email(message=None, send_to=None):
    msg = EmailMessage()
    msg['Subject'] = 'This email has been sent through python script'
    msg['From'] = EMAIL_AD
    msg['To'] = send_to
    if message:
        msg.set_content(message)
    else:
        msg.set_content('Hello friend. My python script actually works')
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_AD, EMAIL_PAS)
        smtp.send_message(msg)

def send_file(filepath=None, message=None, send_to=None):
    if not filepath and send_to:
        return 'Enter path to pdf file and email address'
    msg = EmailMessage()
    msg['Subject'] = 'PDF File'
    msg['From'] = EMAIL_AD
    msg['To'] = send_to
    if message:
        msg.set_content(message)
    else:
        msg.set_content('There is attachment with pdf.')

    with open(filepath, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=f.name)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_AD, EMAIL_PAS)
        smtp.send_message(msg)


if __name__ == '__main__':
    # send_email(send_to=[gmail_address, ya_addr_2])
    # send_email(send_to=[gmail_address])
    send_file(filepath=file_math_py, send_to=[gmail_address, ya_addr_2])