arr = []
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    arr.append(i)

for k in range(1,10001):
    if k in arr:
        pass
    else:
        print(k)

