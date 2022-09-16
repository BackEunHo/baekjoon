from math import sqrt
import sys
# 소수 판별 함수
def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True

m,n = map(int,sys.stdin.readline().split())
for i in range(m,n+1):
    if is_prime_number(i):
        print(i)

