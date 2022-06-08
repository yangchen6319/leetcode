n, k = map(int, input().split())
list1 = [[i for i in map(int, input().split())] for j in range(k)]
temp = set()
errors = 0
for i in range(k):
    if list1[i][1] == 0:
        errors += 1
    elif list1[i][1] in temp:
        errors += 1
    temp.add(list1[i][0])
print(k-errors)
