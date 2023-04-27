import csv
import datetime
import time
from twilio.rest import Client 

# Twilio account SID and auth token
account_sid = 'xxx'
auth_token = 'xxx'
client = Client(account_sid, auth_token)

# Open the CSV file and parse the names and dates
with open('dates.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) #skip header row if there's any
    names = []
    dates = []
    for row in csv_reader:
        name = row[0]
        date = datetime.datetime.strptime(row[1], '%Y-%m-%d')
        names.append(name)
        dates.append(date.strftime('%m-%d'))

# Continuously check for dates and send notifications
while True:
    current_month = datetime.datetime.now().month
    current_day = datetime.datetime.now().day
    for i in range(len(dates)):
        if current_month == int(dates[i][:2]) and current_day == int(dates[i][3:]):
            message = client.messages.create(
                to='+xxx',
                from_='+xxx',
                body=f"Today is {names[i]}'s Birthday! Don't forget to TEXT THEM!"
            )
            print('Message sent at', datetime.datetime.now())
    time.sleep(86400) #wait 24 hours before checking again



