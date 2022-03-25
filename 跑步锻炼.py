import os
import sys
import datetime

# 请在此输入您的代码
star = datetime.date(2000, 1, 1)
end = datetime.date(2020, 10, 1)
day = datetime.timedelta(days = 1)
all = 0
while star <= end:
  if star.day == 1 or star.weekday() == 0:
    all += 2
  else:
    all += 1
  # ！！一定要记住，用while循环一定要加变量值修改，避免死循环
  star += day
print(all)
