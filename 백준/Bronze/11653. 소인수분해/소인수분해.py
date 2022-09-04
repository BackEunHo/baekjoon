n = int(input())
num = 2
while num <= n:
    if n % num == 0:
        n = n // num
        print(num)
    else:
        num += 1
