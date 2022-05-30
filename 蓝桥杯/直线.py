# 求每条直线的斜率和截距，然后去重
# 输入横坐标和纵坐标上限
x, y = map(int, input().split())
# 生成坐标系上的整点
points = [[i, j] for i in range(x) for j in range(y)]
# 创建set容器存放生成的直线
lines = set()
# 求边的斜率和截距
for i in range(len(points) - 1):
  x1, y1 = points[i][0], points[i][1]
  for j in range(i+1, len(points)):
    x2, y2 = points[j][0], points[j][1]
    if x1 == x2:
      continue
    else:
      slope = (y2 - y1)/(x2 - x1)
      inter = (x2 * y1 - x1 * y2) / (x2 - x1)
      if (slope, inter) not in lines:
        lines.add((slope, inter))
print(len(lines) + x)
    
