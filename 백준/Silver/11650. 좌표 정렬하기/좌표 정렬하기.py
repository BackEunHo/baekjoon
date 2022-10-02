import sys
n = int(input())
arr = []
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    arr.append((x,y))
arr.sort()
for j,k in arr:
    print(j, k)

        