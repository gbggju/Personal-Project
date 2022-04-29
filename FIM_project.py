import hashlib
import smtplib
from email.message import EmailMessage

print("Hello, Welcome to the local FIM, please enter the file path you would like to monitor")
filePath = input("Enter file path(ex. /home/downloads/passwords): ")
usrEmail = input("Enter your email")
usrPasswd = input("Enter your password that you set up in your email app password")
print("Make sure two factor authentication is on")



filePath = input("Enter file path(ex. /home/downloads/passwords): ")
def getHash(filePath):
        sha2 = hashlib.sha2
        with open(filePath, 'rb') as file:
            hash = file.read()
            sha2.update(hash)
            return sha2.hexadigest()


def sendEmail():
    alert = EmailMssg()
    alert.set_content(" ")
    alert['subject'] = "one of your files have been tampered with David"
    alert['from'] = usrEmail
    alert['to'] = usrEmail

    user = "chiagochi419@gmail.com"
    password = "DanielC1205*"

    
    server = smptlib.SMTP("smtp.gmail.com", 587)
    server.stattls()
    server.login(user, password)
    server.send_message(message)

    sever.quit()


original = getHash(filePath)
while True:
    check = getHash(filePath)
    if check != original:
        print ("[+] file has been tampered")
    original = check            




#sources:
#https://betterprogramming.pub/how-to-create-a-file-integrity-monitor-with-python-3e4bba66f4cf
#https://www.youtube.com/watch?v=B1IsCbXp0uE
#https://www.youtube.com/watch?v=WJODYmk4ys8&t=375s
#https://www.solarwinds.com/security-event-manager/use-cases/file-integrity-monitoring-software
