from collections import Counter
import sys
n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

#산술평균
print(round(sum(arr) / len(arr)))
arr.sort()
#중앙값
print(arr[n//2])
#최빈값
cnt = Counter(arr).most_common(2)
if len(arr) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
#범위
print(arr[-1] - arr[0])


