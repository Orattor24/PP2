import datetime

today = datetime.datetime.today()

ago = today - datetime.timedelta(days=5)

print(today.strftime("%Y-%m-%d"))
print(ago.strftime("%Y-%m-%d"))
