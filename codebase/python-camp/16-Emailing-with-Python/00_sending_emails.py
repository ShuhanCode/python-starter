#   Sending Emails with Python

import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com',587)    

print(smtp_object.ehlo())

print (smtp_object.starttls())

# For hidden passwords
import getpass

# result = getpass.getpass("Type something here and it will be hidden: ")

# result

email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your password: ")
print(smtp_object.login(email,password))

from_address = email
to_address = email
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")
msg = "Subject: " + subject + '\n' + message

print(smtp_object.sendmail(from_address,to_address,msg))

print(smtp_object.quit())