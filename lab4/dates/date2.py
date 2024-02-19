import datetime

today=datetime.date.today()

delta=datetime.timedelta(days=1)



yest=today-delta

tomor=today+delta

print("yesterday:", yest)
print("today:", today)
print("tomorrow:", tomor)
