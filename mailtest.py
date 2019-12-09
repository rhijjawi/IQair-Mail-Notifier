#!/usr/bin/python
import smtplib
import requests
import time
import json

sender = 'ramzihijjawi@gmail.com'
receivers = ['ramzihijjawi@gmail.com','ammakonnen@isumail.ac.ug','rhijjawi@isumail.ac.ug']
gmail_pass = 'tayyxypbfxmeynzl'
api_key = 'http://api.airvisual.com/v2/nearest_city?lat=0.234261%7D&lon=32.564202%7D&key=5244ee41-e016-4a75-9c7e-e4527229ac08'


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
    message = """From: Ramzi <ramzihijjawi@gmail.com>
To: Mailing List <weather@isumail.ac.ug>
Subject: Air Quality Index Threshold Passed "Potentially Dangerous"

This is a test e-mail message.
"""

    message += 'aqius: ' + str(aqius)
    message += '\nTimestamp: ' + str(timestamp)
    message += '\nMain Pollutant is currently' + str(mainus)
    print('Message Processing completed')

if aqius <= 149:
    print('Current AQI is 100-149')
    message = """From: Ramzi <ramzihijjawi@gmail.com>
To: Mailing List <weather@isumail.ac.ug>
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
