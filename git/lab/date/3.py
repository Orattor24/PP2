import datetime

now = datetime.datetime.now()

new = now.replace(microsecond=0)

print(now)
print(new)
