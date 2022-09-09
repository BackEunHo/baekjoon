n = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = 0
sum = 0
for i in arr:
    sum += i
    result += sum
print(result)