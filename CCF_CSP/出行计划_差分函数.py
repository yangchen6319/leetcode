n, m, k = map(int,input().split())
# 样例输入
list_n = [[i for i in map(int, input().split())] for j in range(n)]
list_m = [[i for i in map(int, input().split())] for j in range(m)]
# 初始化一个差分数列
N = 200001
diff = [0]*N
for sample in list_n:
    l = max(0,sample[0]-k-sample[1]+1)
    r = max(0,sample[0]-k)
    # 修改差分数列表示允许访问的时间段
    diff[l] += 1
    diff[r+1] -= 1
# 利用差分数列求每个时间可以出行的个数
for i in range(1,N):
    diff[i] += diff[i-1]
for j in list_m:
    res = diff[j[0]]
    print(res)