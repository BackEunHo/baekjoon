n = int(input())
find = 0
for i in range(0,n//3 + 1): # 0 <= i <= n//3
    for j in range(0, n//5 + 1): #0 <= j <= n//5
        sum = i*3 + j*5
        if sum == n:
            print(i+j)
            find = 1
            break
    if find == 1:
        break
if find == 0:
    print(-1)
        