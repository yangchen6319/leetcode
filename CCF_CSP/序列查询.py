# 数据输入
n, N = map(int, input().split())
listA = [i for i in map(int, input().split())]
num = 1
sum = 0
for i in range(1,n):
    sum += (listA[i]-listA[i-1])*num
    num += 1
if N > listA[n-1]:
    sum += (N-listA[n-1])*num
print(sum)