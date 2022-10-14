import sys 

def binary_search(arr,key): # arr의 key값의 인덱스를 반환 
    low = 0
    high = len(arr)-1
    while high >= low:
        mid = (low+high) // 2
        if key < arr[mid]:
            high = mid-1
        elif key > arr[mid]:
            low = mid + 1
        else: # key == arr[mid]
            return mid 
    return 'no key' # key not in arr일때

sang_num = int(sys.stdin.readline())
sang_card = list(map(int,sys.stdin.readline().split()))
find_num = int(sys.stdin.readline())
find_card = list(map(int,sys.stdin.readline().split()))

sang_card.sort()
for i in find_card: # [10 9 -5 2 3 4 5 -10]
    if binary_search(sang_card,i) != 'no key':
        print(1, end=' ')
    else:
        print(0, end=' ')
