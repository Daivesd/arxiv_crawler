import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import database_manipulation as dm
import pandas as pd
import time
import datetime

def _convert_time(val):
    date = datetime.datetime.strptime(val,"%Y-%m-%d %H:%M:%S")
    return date
 

df3 = pd.read_pickle('dummydatabase.pkl')

df3['published'] = df3['published'].apply(_convert_time)
    
now = datetime.datetime.now()
delta = datetime.timedelta(days=7)
now - delta

df4 = df3.loc[df3['published'] > (now - delta)]

dm.create_html(df4, 'Last_week_database.html')

with open('Adress_list.txt', 'r') as f:
    toAddress = [line.strip() for line in f]
fromaddr = "Majorana.Arxiv@gmail.com"

Last_week_submissions = open('Last_week_database.html')
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = 'Topo'

msg['Subject'] = "Arxiv Majorana submissions last week"

body = '''Dear topo,

Here is a list of Majorana papers submitted last week. Enjoy reading :)

Regards,
Majorana.Arxiv

''' 

msg.attach(MIMEText(body, 'plain'))
msg.attach(MIMEText(Last_week_submissions.read(),'html'))
Message = msg.as_string()


try:
    conn = smtplib.SMTP('smtp.gmail.com', 587) #smtp address and port
    conn.ehlo() #call this to start the connection
    conn.starttls() #starts tls encryption. When we send our password it will be encrypted.
    conn.login('Majorana.Arxiv@gmail.com', 'Braiding2019')
    conn.sendmail('Majorana_Arxiv@gmail.com', toAddress, Message)
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')
    for i in range(len(toAddress)):
        print(toAddress[i])
except smtplib.SMTPException:
    print('Error: Failed to send mail.')
    