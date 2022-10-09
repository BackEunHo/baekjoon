def push(n): #정수 n을 스택에 넣음
    arr.append(n)

def pop(): # 스택의 가장 위의 정수를 빼고, 출력한다. 빈 경우에는 -1 출력
    if len(arr) == 0:
        print(-1)
    else:
        print(arr.pop())

def size():
    print(len(arr))

def empty():
    if len(arr) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[-1])

import sys
arr = []
t = int(sys.stdin.readline())
cnt = 0
while(cnt<t):
    input = sys.stdin.readline().split()
    if input[0] == 'push':
        push(input[1])
    elif input[0] == 'pop':
        pop()
    elif input[0] == 'size':
        size()
    elif input[0] == 'empty':
        empty()
    else:#top
        top()
    cnt+=1

