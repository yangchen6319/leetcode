count = 0
i = 1
while True:
  count += str(i).count('1')
  if count >= 2021:
    print(i)
    break
  i += 1

