t = int(input())
for _ in range(t):
    h,w,n = map(int,input().split())
    if n % h == 0: #a = 층수
        a = h
    else:
        a = n % h
    if n % h == 0: # b = 호수
        b = n // h 
    else:
        b = n // h +1
    if b < 10:
        print(f'{a}0{b}')
    else:
        print(f'{a}{b}')