import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    arr.append([age,name])
arr.sort(key = lambda x:x[0]) 
#[[20, 'Sunyoung'], [21, 'Junkyu'] ,[21, 'Dohyun']]

for i in arr:
    print(i[0], i[1])

# python은 stable 정렬(입력 받은 값들 중 값은 값이 있는 경우 해당 값의 순서를 그대로 유지)