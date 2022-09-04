def hansu(n):
    hansu_cnt = 0
    for i in range(1,n+1):
        hansu_arr = list(map(int,str(i)))
        if i < 100:
            hansu_cnt += 1
        else:
            if hansu_arr[0] - hansu_arr[1] == hansu_arr[1] - hansu_arr[2]:
                hansu_cnt += 1
    return hansu_cnt 

n = int(input())
print(hansu(n))