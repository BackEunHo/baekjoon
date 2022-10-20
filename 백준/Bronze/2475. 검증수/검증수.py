import sys 

arr = list(map(int,sys.stdin.readline().split()))
sum = 0
for i in arr:
    sum += i**2
print(sum % 10)
