row = 1
col = 1
flag = 1
num = 1
# 暴力破解蛇形填数问题，主要按照条件进行循环累加
while True:
  if row == 1:
    col += 1
    flag = 1
    num += 1
  if col == 1:
    row += 1
    flag = -1
    num +=1
  row += flag
  col -= flag
  num += 1
  if row == 20 and col == 20:
    break
print(num)