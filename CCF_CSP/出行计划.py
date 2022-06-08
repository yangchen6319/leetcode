n, m, k =  map(int, input().split(' '))
list_n = [[i for i in map(int, input().split())] for j in range(n)]
list_m = [[i for i in map(int, input().split())] for j in range(m)]
for i in range(m):
    times = 0
    get_time = list_m[i][0] + k
    for j in range(n):
        if get_time <= list_n[j][0] and get_time + list_n[j][1] > list_n[j][0]:
            times += 1
    print(times)