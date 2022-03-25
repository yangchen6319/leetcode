import os
import sys

# 请在此输入您的代码
n = int(input())
num = []
mean = 0
for i in range(n):
  x = int(input())
  mean += x
  num.append(x)
mean = mean/n+0.005
print(max(num))
print(min(num))
print("{:.2f}".format(mean))