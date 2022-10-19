def fac(num):
    count = 1
    for i in range(2,num+1):
        count *= i
    return count
import sys
n = int(sys.stdin.readline())
fac_n = list(map(int, str(fac(n)))) # 입력한 수의 factorial
cnt = 0
for i in range(len(fac_n)-1,-1,-1):
    if fac_n[i] == 0:
        cnt += 1
    else:
        print(cnt)
        break