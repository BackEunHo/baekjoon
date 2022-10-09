import sys

arr = []
t = int(sys.stdin.readline())
sum = 0
for i in range(t):
    n = int(sys.stdin.readline())
    if n == 0:
        sum = sum - arr[-1]
        arr.pop()
    else:
        arr.append(n)
        sum += n
print(sum)