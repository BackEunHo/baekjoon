import sys
while True: 
    a = list(map(int,sys.stdin.readline().split()))
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    max_num = max(a)
    a.pop(a.index(max_num))
    if max_num**2 == a[0]**2 + a[1]**2:
        print('right')
    else:
        print('wrong')
