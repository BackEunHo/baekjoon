import sys
cnt = 0
sum = 0
while cnt < 5:
    num = int(sys.stdin.readline())
    if num < 40:
        num = 40
    sum += num
    cnt += 1
print(sum//5)