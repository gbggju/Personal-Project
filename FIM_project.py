


import hashlib
import smtplib
from email.message import EmailMessage

print("Hello to local FIM, please enter the file path to monitor")
filePath = input("Enter file path(ex. /home/downloads/passwords): ")
usrEmail = input("Enter your email")
usrPasswd = input("Enter your password")
print("Make sure two factor authentication is on")
def getHash(filePath):
    sha256 = hashlib.sha256()
    with open(filePath,'rb') as file:
        hash = file.read()
        sha256.update(hash)
        return sha256.hexdigest()
from email.message import EmailMessage

def sendEmail():
    message = EmailMessage()
    message.set_content(" ")
    message['subject'] = "file has ben altered"
    message['from'] = usrEmail
    message['to'] = usrEmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(usrEmail, usrPasswd)
    server.send_message(message)
    server.quit()

baseline = getHash(filePath)
print("[+] Just calculated your baseline")
print("[+] Checking")
while True:
    check = getHash(filePath)
    if check != baseline:
        sendEmail()
        print("[+] Someone edited the file")
        baseline = check

# https://www.youtube.com/watch?v=B1IsCbXp0uE
# #https://www.youtube.com/watch?v=WJODYmk4ys8&t=375s
# #https://www.solarwinds.com/security-event-manager/use-cases/file-integrity-monitoring-software
# https://sciencevikinglabs.com/blog/security/2015-10-03-building-a-basic-file-integrity-monitor/

