import imapclient
import email
import pprint
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

def read_messages():
    with imapclient.IMAPClient('imap.gmail.com', ssl=True) as imapObj:
        imapObj.login(EMAIL_AD, EMAIL_PAS)
        imapObj.select_folder('INBOX', readonly=True)
        uids = imapObj.search('UNSEEN')
        raw_messages = imapObj.fetch([uids[-4]], ['BODY[]', 'FLAGS'])  # uids[-3] - 3td from above
        import pyzmail
        message = pyzmail.PyzMessage.factory(raw_messages[uids[-4]][b'BODY[]'])
        
        print(message.get_subject())
        print(f'From: {message.get_addresses("from")}')
        print(f'To: {message.get_addresses("to")}')
        print(f"cc: {message.get_addresses('cc')}")
        print(f"bcc: {message.get_addresses('bcc')}")
        print(f"message.text_part != None => {message.text_part != None}")
        print(message.text_part.get_payload().decode(message.text_part.charset))
        print(message.html_part != None)
        print('='*100)
        pprint.pprint(message.html_part.get_payload().decode(message.html_part.charset))
