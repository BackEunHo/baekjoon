import sys 

n,m = map(int,sys.stdin.readline().split())
cnt = 0
result = 0
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().strip()) # ['mybaekjoononline', 'conding', 'mouse']

while cnt<m:
    string = sys.stdin.readline().strip()# baekjoon, codeplus....
    if string in arr:
        result += 1
    cnt += 1
print(result)
    