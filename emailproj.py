import smtplib
import time
from datetime import datetime
import pytz

p_word = input('Input your password: ')

def prep_email():
    print('Preparing SMTP...')

    mail_obj = smtplib.SMTP('smtp.gmail.com',587)
    mail_obj.ehlo()
    mail_obj.starttls()

    e_mail = 'ramoj845@gmail.com'

    mail_obj.login(e_mail,p_word)
    print('Login Successful!')

    from_add = 'ramoj845@gmail.com'
    to_add = 'ramoj845@gmail.com'

    subj = 'DONT FORGET YOUR STREAKS'
    body = 'DONT FORGET YOUR STREAKS'

    msg = f'Subject:{subj}\n{body}'

    mail_obj.sendmail(from_add,to_add,msg)
    print('Message Sent!')

    mail_obj.quit()

while True:

    tz = pytz.timezone('Asia/Singapore')
    now = datetime.now(tz)

    if now.hour == 0 and now.minute == 0 and now.second == 0:
        prep_email()
        continue

    time.sleep(1)   





    












