import datetime

mytime = datetime.time(2, 20)

print(mytime.minute)

print(mytime.hour)

# print(mytime)

print(type(mytime))

today = datetime.date.today()

print(today)

print(today.year)

print(today.month)

print(today.ctime())

from datetime import datetime

mydatetime = datetime(2021, 10, 3, 14, 20, 1)

print(mydatetime) # 2021-10-03 14:20:01

print(mydatetime.replace(year=2020)) # 2020-10-03 14:20:01

date1 = datetime(2021, 11, 3, 22, 0)

date2 = datetime(2020, 11, 3, 12, 0)

result = date1 - date2

type(result) # datetime.timedelta

# print(result.days) # 365

datetime1 = datetime(2021, 11, 3, 22, 0)

datetime2 = datetime(2020, 11, 3, 12, 0)

print(datetime1 - datetime2) # 365 days, 10:00:00

mydiff = datetime1 - datetime2

print(mydiff.seconds) # 36000

print(mydiff.total_seconds()) # 31572000.0

