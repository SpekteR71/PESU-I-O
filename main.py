import csv
from http import server
import smtplib
from email.message import EmailMessage

sender_address ='pesuio.sme@pes.edu'       #Sender Email Login         
sender_pass ='pesupersonnel@123'                       #Sender Email Password
subject = 'Week-1 Summary Video - Revised Link'           #Subject of the mail


#Follow ' https://myaccount.google.com/lesssecureapps ' and login with the sender email credentials and Enable 'Allow less secure apps: ON'.

with open('list.csv', "r", encoding = "utf-8", errors = "ignore") as csvfile: #csv file named as 'list.csv' in same directory as py file with format (Email,Name,Postion)
    reader = csv.reader(csvfile)
    reader = csv.reader(x.replace('\0', '') for x in csvfile)
    for line in reader:
        text = 'Greetings from PESU I/O!' + '''

We have successfully started with the first week of Slot 14 and we hope you are loving the peer to peer teaching.

Please find the link for the Week 1 summary video attached below. We request you to share the link with your students on the Whatsapp group by EOD.

Video Link:''' + line[3] + '''
        
Your friendly neighborhood Personnel Management team
PESU I/O
#LearnDifferently
'''
        #print(text)

        email_send = line[1]
        msg = EmailMessage()
        msg['From'] = sender_address
        msg['To'] = email_send
        msg['Subject'] = subject
        msg.set_content(text)

        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(sender_address,sender_pass)
        server.send_message(msg)

        server.quit()

print('Emails sent successfully.')
