import sys

def gcd(x,y):
    while y:
        x, y = y, x % y
    return x 
t = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
for i in range(t-1):
    print(f'{arr[0]//gcd(arr[0],arr[i+1])}/{ arr[i+1] // gcd(arr[0],arr[i+1])}')
