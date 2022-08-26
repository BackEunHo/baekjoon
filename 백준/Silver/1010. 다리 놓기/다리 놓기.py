def fac(a):
    num = 1 
    for i in range(1,a+1):
        num *= i
    return num

a = int(input())

for i in range(a):
    n,m = map(int,input().split())
    print(fac(m) // (fac(n) * fac(m-n)))