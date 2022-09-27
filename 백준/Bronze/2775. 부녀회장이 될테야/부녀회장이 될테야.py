t = int(input())
for _ in range(t):
    k = int(input()) # k층
    n = int(input())# n호
    arr = list(range(1,n+1)) # 0층의 1~n호의 인원 수 할당
    sum = 0
    for i in range(k):
        for j in range(1,n):
            arr[j] = arr[j-1]+arr[j]
    print(arr[n-1])

        
            

