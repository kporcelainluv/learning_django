import datetime

year, month, day = input().split()

date_given = datetime.date(int(year), int(month), int(day))
#2016 4 20
what_we_add = int(input())
delta = datetime.timedelta(days=what_we_add)
now_date = date_given + delta
print(now_date.year,now_date.month, now_date.day )
