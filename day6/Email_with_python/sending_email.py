import smtplib
import getpass
smtp_obj =  smtplib.SMTP('smtp.gmail.com',587)
print(smtp_obj.ehlo())
print(smtp_obj.starttls())
email = getpass.getpass("email : ")
password = getpass.getpass("Password :")
print(smtp_obj.login(email,password))
from_email_add = email
to_dest = input("enter the destination email : ")
subject = input("enter subject\n")
message = input("enter message")
msg = "Subject : "+subject+'\n' +message
smtp_obj.sendmail(from_email_add,to_dest,msg)
print(smtp_obj.quit())