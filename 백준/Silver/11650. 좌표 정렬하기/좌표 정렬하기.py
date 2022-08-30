n = int(input())
arr = []
for i in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

quick_sort_arr = quick_sort(arr)

for j in range(len(quick_sort_arr)):
    for k in range(2):
        print(quick_sort_arr[j][k], end=' ')
    print()

        