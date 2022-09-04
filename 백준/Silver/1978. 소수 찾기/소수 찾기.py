n = int(input()) # 4 
arr = list(map(int,input().split())) # 1 3 5 7
cnt = 0

for num in arr:
    find = 0
    if num > 1:
        for i in range(2,num):
            if num % i ==0: # 소수가 아니라면
                find += 1
        if find == 0:
            cnt += 1

print(cnt)

