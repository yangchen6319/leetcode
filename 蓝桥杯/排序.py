import os
import sys

# 请在此输入您的代码
# 1 字符串最短
# 2 字典序最小
# 3 没有重复字母
# 因为N个字符进行冒泡排序，交换次数最多为N(N-1)/2
# 计算N
N = 0
for i in range(1,27):
  if i*(i-1) > 200:
    N = i
    break
# N为15 表示字符串有15个字母
# 因此字符串为onmlkjihgfedcba
# 因为要排序100次且字典序最小，所以把第6位j提到第一位，既能保证字典序最小又能减少5次交换
print('jonmlkihgfedcba')