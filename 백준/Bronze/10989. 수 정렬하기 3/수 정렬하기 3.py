import sys
t = int(input())
arr = [0] * 10001
for i in range(t):
    n = int(sys.stdin.readline())
    arr[n] = arr[n]+1
    
for j in range(10001):
    if arr[j] != 0:
        for k in range(arr[j]):
            print(j)