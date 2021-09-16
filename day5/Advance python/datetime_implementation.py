import datetime

now_time = datetime.time(2,20)
print(now_time.hour)
print(now_time.minute)

today_date = datetime.date.today()
print(f'today\'s date  = {today_date}')
print(f'Year = {today_date.year}')
print(f'month =  {today_date.month}')
print(f'day = {today_date.day}')

mydatatime = datetime.datetime(2020,9,14,15,15)
mydatatime1 = datetime.datetime(2021,9,14,15,10)

mydiffer =  mydatatime1 - mydatatime
print(mydiffer.days)

