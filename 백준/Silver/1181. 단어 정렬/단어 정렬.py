import sys
n = int(input())
arr = []
for _ in range(n): # 문자 입력
    arr.append(sys.stdin.readline().strip())
arr = list(set(arr))
arr.sort()
arr.sort(key = len)

for i in arr:
    print(i)
