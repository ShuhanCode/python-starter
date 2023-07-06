import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')

import getpass

email = getpass.getpass("Email: ")
 
password = getpass.getpass("Password: ")
 
print ( M.login(email,password))

print(M.list())

print(M.select("inbox"))