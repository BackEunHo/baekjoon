cnt = 0
def recursion(s, l, r,cnt):
    cnt += 1
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1,cnt)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1,cnt)

n = int(input())
for i in range(n):
    word = input()
    a,b = isPalindrome(word)
    print(a,b)

