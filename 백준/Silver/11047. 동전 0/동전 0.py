n,k = map(int,input().split())
arr = []
cnt = 0
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

while True:
    for j in arr:
        if j <= k:
            count = k // j
            k = k % j
            cnt += count
    if k == 0:
        break
print(cnt)
