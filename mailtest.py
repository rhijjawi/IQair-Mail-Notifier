#!/usr/bin/python
import smtplib
import requests
import time
import json

sender = '***@gmail.com'
receivers = ['example@gmail.com','***@example.com','***@example.ac.ug']
# use an App-Specific Password for this
gmail_pass = '' 
api_key = 'KEY GOES HERE'


response = requests.get(api_key)
data = response.json()
aqius = data['data']['current']['pollution']['aqius']
timestamp = data['data']['current']['pollution']['ts']
mainus = data['data']['current']['pollution']['mainus']
print (aqius)
print (timestamp)
print (mainus)

if aqius > 150:
    print('Current AQI is greater than 150')
    message = """From: ***** <*****@gmail.com>
To: Mailing List <***@***.ac.ug>
Subject: Air Quality Index Threshold Passed "Potentially Dangerous"

This is a test e-mail message.
"""

    message += 'aqius: ' + str(aqius)
    message += '\nTimestamp: ' + str(timestamp)
    message += '\nMain Pollutant is currently' + str(mainus)
    print('Message Processing completed')

if aqius <= 149:
    print('Current AQI is 100-149')
    message = """From: Ramzi <****@gmail.com>
To: Mailing List <****@****.ac.ug>
Subject: Air Quality Index Threshold Passed ""

This is a test e-mail message.
"""

    message += 'aqius: ' + str(aqius)
    message += '\nTimestamp: ' + str(timestamp)

    if mainus == str(mainus):
        message += '\nMain Pollutant is currently' + str(mainus)

print('Message Processing completed')

with open('graph.txt', 'a') as file:
    file.write(timestamp)
    file.write(aqius)
    file.write('\n')

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.ehlo()
   smtpObj.login(sender, gmail_pass)
   smtpObj.sendmail(sender, receivers, message)
   smtpObj.quit()
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")
