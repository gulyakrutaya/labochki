import datetime

today=datetime.date.today()

delta=datetime.timedelta(days=5)

result=today-delta

print("today is:", today)
print("new date:", result)