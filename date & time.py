import datetime
date = datetime.date(2026,7,30)
today = datetime.time(12,34,40)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %D")
print (date)
print (today)
print(now)