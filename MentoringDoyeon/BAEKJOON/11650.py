import sys

N = int(sys.stdin.readline())
grid_list = list(list(map(int, sys.stdin.readline().split())) for _ in range(N)) #이중리스트로 받기

def bubble_sort(array):
    count = 1
    while count != 0:
        count = 0
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                count += 1
            else:
                pass

def selection_sort(array):
    for i in range(len(array)):
        min = array[i]
        for j in range(i, len(array)): #최솟값 찾기
            if array[j] < min:
                min = array[j]
                min_index = j
        if min == array[i]: #만약 최솟값이 자기자신이면 pass
            pass
        else: #아니면 자리 바꾸기
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp

def insert_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        for j in range(i-1, -1, -1): #key 이전값들 하나씩 비교
            if array[j] > key:
                array[j+1] = array[j]
            else: #만약 크거나 같으면 반복종료
                break
            array[j] = key

def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    array = merge(array, left, right)

    return array

def merge(array, left, right):
    p, q, t = 0, 0, 0
    while p < len(left) and q < len(right):
        if left[p] < right[q]:
            array[t] = left[p]
            p += 1
        else:
            array[t] = right[q]
            q += 1
        t += 1

    while p < len(left):
        array[t] = left[p]
        t += 1
        p += 1

    while q < len(right):
        array[t] = right[q]
        t += 1
        q += 1

    return array

def quick_sort(array):
    if len(array) <= 1: return array

    mid = len(array) // 2

    less, equal, big = [], [], []
    for i in range(len(array)):
        if array[i] < array[mid]:
            less.append(array[i])
        elif array[i] > array[mid]:
            big.append(array[i])
        else:
            equal.append(array[mid])
    less = quick_sort(less)
    equal = quick_sort(equal)
    big = quick_sort(big)

    array = less + equal + big
    return array

# bubble_sort(grid_list)
# selection_sort(grid_list)
# insert_sort(grid_list)
merge_sort(grid_list)
grid_list = quick_sort(grid_list)

for g in grid_list: #결과출력
    for gg in g:
        print(gg, end=' ')
    print('')