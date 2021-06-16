import imapclient
import email
from email.message import EmailMessage
from confidential import gmail_address, gmail_pas



EMAIL_AD = gmail_address
EMAIL_PAS = gmail_pas

def mail_info():
    """Number of messages in INBOX."""
    with imapclient.IMAPClient('imap.gmail.com', ssl=True) as imapObj:
        imapObj.login(EMAIL_AD, EMAIL_PAS)
        select_info = imapObj.select_folder('INBOX', readonly=True)
        messages_num = select_info[b'EXISTS']
    return '{} messages in INBOX'.format(messages_num)

def unread_email():
    """Download unread emails and parse them into 
    standard EmailMessage objects."""
    with imapclient.IMAPClient('imap.gmail.com', ssl=True) as imapObj:
        imapObj.login(EMAIL_AD, EMAIL_PAS)
        imapObj.select_folder('INBOX', readonly=True)
        messages = imapObj.search(["UNSEEN"])
        for uid, message_data in imapObj.fetch(messages, "RFC822").items():
            email_message = email.message_from_bytes(message_data[b"RFC822"])
            print(uid, email_message.get('From'), email_message.get('Subject'))
