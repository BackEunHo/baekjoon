import sys 

n,m = map(int,sys.stdin.readline().split())
a = set(map(int,sys.stdin.readline().split()))
b = set(map(int,sys.stdin.readline().split()))
result1 = a-b
result2 = b-a
print(len(result1) + len(result2))