import datetime
import time

# n = int(input())
# # 将输入的数字转换为秒
# n = int(n/1000)
# # 提取time
# n = n%(3600*24)
# # 提取小时数
# h = int(n/3600)
# # 提取分钟数
# m = int((n%3600)/60)
# # 提取秒钟数
# s = n%60
# # 根据输入生成一个time
# t = datetime.time(hour = h, minute = m, second = s)
# print(t)

# 第二种方式
n = int(input())
t = time.asctime(time.gmtime(n/1000))
print(t[11:19])
