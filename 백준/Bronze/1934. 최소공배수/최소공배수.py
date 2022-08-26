def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

n = int(input())
arr_n = []
for i in range(n):
    x,y = map(int,input().split())
    arr_n.append((x,y))

for j in arr_n:
    print(int(j[0]*j[1] / gcd(j[0],j[1])))