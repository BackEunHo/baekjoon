import sys
while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break
  cnt = 0
  for i in range(n+1,2*n + 1):
      if i == 2:
        cnt += 1
        continue
      else:
        for j in range(2,int(i**0.5)+1):
          if i % j == 0:
            break
        else:
          cnt += 1
  print(cnt)