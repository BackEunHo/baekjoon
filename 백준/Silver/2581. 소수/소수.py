m = int(input())
n = int(input())

m2n_arr = list(range(m,n+1)) # 60 ~ 100
sosu_list = []
sum = 0

for num in m2n_arr:
    find = 0
    if num > 1:
        for i in range(2,num):
            if num % i ==0: # 소수가 아니라면
                find += 1
        if find == 0:
            sum += num
            sosu_list.append(sum)

if len(sosu_list) == 0:
    print(-1)
else:
    print(sum)
    print(min(sosu_list))
