import datetime

today = datetime.datetime.today()

yesterday = today - datetime.timedelta(days=1)
tomorow = today + datetime.timedelta(days=1)

print(today.strftime("%Y-%m-%d"))
print(yesterday.strftime("%Y-%m-%d"))
print(tomorow.strftime("%Y-%m-%d"))
