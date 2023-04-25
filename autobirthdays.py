import csv
import datetime
import time
from twilio.rest import Client 

# Twilio account SID and auth token
account_sid = 'AC8fe443806b782ae0a6881a80f23a78c5'
auth_token = '472f1c10001fdc5d72ffc341b9da7941'
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
                to='+14694694593',
                from_='+18776294436',
                body=f"Today is {names[i]}'s Birthday! Don't forget to TEXT THEM!"
            )
            print('Message sent at', datetime.datetime.now())
    time.sleep(86400) #wait 24 hours before checking again



