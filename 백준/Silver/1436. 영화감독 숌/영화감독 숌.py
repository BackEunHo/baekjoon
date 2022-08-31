n = int(input())
cnt = 0
num = 665
while(cnt <n):
    result = list(map(int,str(num)))
    for i in range(0,len(result)-2):
        if result[i] ==  result[i+1] == result[i+2] and result[i] + result[i+1] + result[i+2] ==18 :
            cnt += 1
            break
    num += 1
print(num-1)