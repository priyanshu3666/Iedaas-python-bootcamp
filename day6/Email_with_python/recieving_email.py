import imaplib
import email
import getpass
M = imaplib.IMAP4_SSL('imap.gmail.com')
user = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
M.login(user,password)
M.select("inbox")
typ ,data = M.search(None,'SUBJECT "virca is you me myself"')
result, email_data = M.fetch(data[0],"(RFC822)")
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)