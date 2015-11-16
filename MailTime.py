#! usr/bin/ env python3


import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com')
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('abdielhmelendez@gmail.com', 'hilltop123')
smtpObj.sendmail('abdielhmelendez@gmail.com', 'abdielhmelendez@gmail.com'
  , 'Subject: So long.')
smtpObj.quit()
