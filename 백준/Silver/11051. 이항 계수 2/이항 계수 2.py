n,m = map(int,input().split())

def fac(a):
    num = 1 
    for i in range(1,a+1):
        num *= i
    return num

if m<0:
    print(0)
elif 0<=m and m<=n:
    print(fac(n) // (fac(m) * fac(n-m)) % 10007)
else:
    print(0)
