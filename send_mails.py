import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import pandas as pd
import database_manipulation as dm

def _convert_time(val):
    date = datetime.datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
    return date

def sendemail():
    database_df = pd.read_pickle('dummydatabase.pkl')
    
    database_df['published'] = database_df['published'].apply(_convert_time)
        
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=7)
    # now - delta
    
    database_lastweek_df = database_df.loc[database_df['published'] > (now - delta)]
    
    dm.create_html(database_lastweek_df, 'Last_week_database.html')
    
    with open('Adress_list.txt', 'r') as f:
        toAddress = [line.strip() for line in f]
    fromaddr = "thearxivscraper@gmail.com"
    
    Last_week_submissions = open('Last_week_database.html')
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = 'Me'
    
    msg['Subject'] = "Arxiv submissions last week"
    
    body = '''Hi,
    
    Testing the email.
    
    ''' 
    
    msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(Last_week_submissions.read(),'html'))
    Message = msg.as_string()
    
    
    # try:
    conn = smtplib.SMTP('smtp.gmail.com', 587) #smtp address and port
    conn.ehlo() #call this to start the connection
    conn.starttls() #starts tls encryption. When we send our password it will be encrypted.
    conn.login('thearxivscraper@gmail.com', 'xopb uted vhjs raeb')
    conn.sendmail('thearxivscraper@gmail.com', toAddress, Message)
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')
    for i in range(len(toAddress)):
        print(toAddress[i])
    # except smtplib.SMTPException:
    #     print('Error: Failed to send mail.')
    
