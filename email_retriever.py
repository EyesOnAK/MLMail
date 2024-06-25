# email_retriever.py

import os
import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL_SERVER = os.getenv('EMAIL_SERVER')

def connect_to_email():
    # Connect to the server
    mail = imaplib.IMAP4_SSL(EMAIL_SERVER)
    # Login to your account
    mail.login(EMAIL_USER, EMAIL_PASS)
    return mail

def fetch_emails(mail):
    # Select the mailbox you want to use
    mail.select("inbox")
    pass
    
    # Search for all emails in the inbox
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    emails = []
    for email_id in email_ids:
        # Fetch the email by ID
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                # Decode email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                # Decode email sender
                from_ = msg.get("From")
                # Print the subject and sender
                print("Subject:", subject)
                print("From:", from_)
                emails.append({
                    "subject": subject,
                    "from": from_,
                    "body": get_email_body(msg)
                })
    return emails

def get_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode()
    else:
        return msg.get_payload(decode=True).decode()

if __name__ == "__main__":
    mail = connect_to_email()
    emails = fetch_emails(mail)
    for email in emails:
        print(email)
