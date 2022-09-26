n = int(input())
for i in range(n): # 1~n 까지 전체 
    result = sum(map(int,str(i))) 
    result += i
    if result == n:
        print(i)
        break
else:
    print(0)
