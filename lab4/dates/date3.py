import datetime

now=datetime.datetime.today()

new_date=now.replace(microsecond=0)

print("date_time with ms:", now)

print("date_time without ms:", new_date)