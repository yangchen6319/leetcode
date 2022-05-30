# 暴力枚举，枚举长度为10的等差数列，其成员全为素数即可
# 定义函数用来判断是否是素数
def isPrime(a):
  for i in range(2,a):
    if a%i == 0:
      return False
  return True

# 枚举等差数列的首项
for i in range(2,1000):
  if !isPrime(i):
    continue
  else:
    for j in range(1,501):
      # 找个长度为10的等差数列
      for f in range(10):
        if !isPrime(i+j*f):
          break
        else if f == 9:
          print(j)
          

