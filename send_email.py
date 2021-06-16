import smtplib
from email.message import EmailMessage
from confidential import gmail_address, gmail_pas, ya_addr_1, ya_addr_2, file_math_py
from confidential import html_content, mult

EMAIL_AD = gmail_address
EMAIL_PAS = gmail_pas


def send(message):
    """
    Send message by SMTP.
    Service func for 'send_email()', 'send_file()', 'send_html'. 
    """
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_AD, EMAIL_PAS)
        smtp.send_message(message)


def send_email(message=None, send_to=None, subject=None):
    """
    Send text message in 'message' var.
    """
    msg = EmailMessage()
    msg['Subject'] = subject if subject else 'This is email'
    msg['From'] = EMAIL_AD
    msg['To'] = send_to
    if message:
        msg.set_content(message)
    else:
        msg.set_content('Hello friend. This email sent by python script.')
    send(msg)
    return "Email sent"


def send_file(filepath=None, message=None, send_to=None, subject=None):
    """
    Send file with message.
    """
    if not (filepath and send_to):
        return 'Enter path to a file and email address'
    msg = EmailMessage()
    msg['Subject'] = subject if subject else 'File attached'
    msg['From'] = EMAIL_AD
    msg['To'] = send_to
    if message:
        msg.set_content(message)
    else:
        msg.set_content('Hello friend. This email sent by python script')

    with open(filepath, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=f.name)
    send(msg)
    return "File sent"


def send_html(message=None, send_to=None, subject=None):
    "Send email message with html tags."
    msg = EmailMessage()
    msg['Subject'] = subject if subject else 'Here is mail with html.'
    msg['From'] = EMAIL_AD
    msg['To'] = send_to
    if message:
        msg.set_content(message, subtype='html')
    else:
        msg.set_content(html_content, subtype='html')
    send(msg)
    return "Email with html sent"
    


if __name__ == '__main__':
    # send_email(send_to=[gmail_address, ya_addr_2])
    # send_email(send_to=[gmail_address])
    # send_html(send_to=[gmail_address, ya_addr_2])
