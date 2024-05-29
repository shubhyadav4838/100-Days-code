import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() # Tell us the day of week in integer
print(day_of_week)
date_of_birth =dt.datetime(year = 2005, month = 2, day = 19, hour = 4)
print(date_of_birth)

