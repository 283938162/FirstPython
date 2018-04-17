# import time
#
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))


# 获取指定日期的前一天后一天
import datetime

today = datetime.date.today()

print(today)

tomorrow = today+datetime.timedelta(days = 1)

print(tomorrow)

the_day_after = today+datetime.timedelta(days = 2)
print(the_day_after)