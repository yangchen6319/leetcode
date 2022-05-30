import math

# 求最小公倍数
def lcm(a, b):
  return a * b // math.gcd(a, b) #math.gcd求最小公倍数

# 输入节点数量
n = int(input())

dp = [float('inf')]*(n+1)
dp[1] = 0
for i in range(1, n + 1):
  for j in range(i+1, i+22):
    if j > n:
      break
    dp[j] = min(dp[j], dp[i] + lcm(i, j))
print(dp[n])