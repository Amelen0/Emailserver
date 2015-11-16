#! usr/bin/ env python3


import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com')
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('xxxxxxxx@gmail.com', 'xxxxxxx')
smtpObj.sendmail('xxxxxxx@gmail.com', 'xxxxxxxx@gmail.com'
  , 'Subject: So long.')
smtpObj.quit()
