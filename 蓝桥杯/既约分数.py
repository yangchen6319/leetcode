import math

count = 0
# 在1-2020范围内找到最大公约数为1的数
for i in range(1, 2021):
  for j in range(i+1, 2021):
    if math.gcd(i,j) == 1:
      count += 1
print(count*2)
