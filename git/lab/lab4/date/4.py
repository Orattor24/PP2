import datetime


date1 = datetime.datetime(2024, 1, 29, 12, 0, 0)
date2 = datetime.datetime(2024, 1, 28, 12, 0, 0)

difference_in_seconds = abs((date1 - date2).total_seconds())

print(difference_in_seconds)
