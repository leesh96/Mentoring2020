import sys


def mergesort(array):   # 병합정렬
    if len(array) <= 1:
        return array

    mid_index = len(array) // 2

    left = mergesort(array[:mid_index])     # 전반부 정렬
    right = mergesort(array[mid_index:])    # 후반부 정렬
    array = merge(array, left, right)       # 병합

    return array


def merge(array, left, right):  # 병합
    p, q, t = 0, 0, 0

    while p < len(left) and q < len(right):
        if left[p][0] < right[q][0]:
            array[t] = left[p]
            p += 1
        elif left[p][0] == right[q][0]:
            if left[p][1] < right[q][1]:
                array[t] = left[p]
                p += 1
            else:
                array[t] = right[q]
                q += 1
        else:
            array[t] = right[q]
            q += 1
        t += 1

    while p < len(left):    # 왼쪽 배열 남았으면
        array[t] = left[p]
        t += 1
        p += 1

    while q < len(right):   # 오른쪽 배열 남았으면
        array[t] = right[q]
        t += 1
        q += 1

    return array


size = int(sys.stdin.readline())
num = []

for i in range(size):
    num.append(tuple(map(int, sys.stdin.readline().split())))

num = mergesort(num)

for i in range(size):
    print(num[i][0], num[i][1], sep=" ")