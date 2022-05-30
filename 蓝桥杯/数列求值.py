# 暴力求一下
a, b, c, d = 1, 1, 1, 0
for i in range(4,20190325):
  d = (a + b + c)%10000
  a, b, c = b, c, d
print(c)