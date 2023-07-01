import datetime

mytime = datetime.time(2, 20)

print(mytime.minute)

print(mytime.hour)

print(mytime)

print(type(mytime))

today = datetime.date.today()

print(today)

print(today.year)

print(today.month)

print(today.ctime())

from datetime import datetime

print(datetime())