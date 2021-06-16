import imapclient
import email
from email.message import EmailMessage
from confidential import gmail_address, gmail_pas



EMAIL_AD = gmail_address
EMAIL_PAS = gmail_pas

def mail_info():
    """Number of messages in INBOX."""
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imapObj.login(EMAIL_AD, EMAIL_PAS)
    select_info = imapObj.select_folder('INBOX', readonly=True)
    messages_num = select_info[b'EXISTS']
    imapObj.logout()
    return '{} messages in INBOX'.format(messages_num)

def unread_email():
    """Download unread emails and parse them into 
    standard EmailMessage objects."""
    pass