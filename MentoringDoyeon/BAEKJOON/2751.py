'''11/10 여러가지 정렬'''
import sys


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

N = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline().strip()) for x in range(N)]

# bubble_sort(input_list)
# selection_sort((input_list))
# insert_sort(input_list)
# merge_sort(input_list)
input_list = quick_sort(input_list) #새로운 리스트를 만든거라(?) 대입해줘야함

print('\n'.join(map(str, input_list)))


'''함수 이용'''
# import sys
#
# N = int(sys.stdin.readline())
# num_list = []
# for _ in range(N):
#     num_list.append(int(sys.stdin.readline()))
#
# num_list = sorted(num_list) # 오름차순으로 정렬
# for v in num_list:
#     print(v)


'''함수 없이 - 런타임 에러'''
# import sys

# N = int(sys.stdin.readline()) #sys.stdin 이 더 빠름
# input_list = []
# for _ in range(N):
#     input_list.append(int(sys.stdin.readline()))

# result_list = []
# result_list.append(input_list[0])
# for input_index in range(1, N): # 인덱스로 num_list를 순서대로 꺼내기 위한 반복문. 최초 1개 추가했으니 1부터
#     for result_index in range(len(result_list)): #result_list 요소를 탐색할 거니까 result_list 길이 만큼 반복
#         '''result_list의 요소랑 하나씩 비교해서 만약 작은 수를 만나면 앞에 추가하고 아니면 작은 수를 만날 때 까지 반복.
#         끝까지 작은 수를 못만나면 result_list중 가장 큰 수 이므로 맨 마지막에 추가'''
#         if input_list[input_index] < result_list[result_index]:
#             result_list.insert(result_index, input_list[input_index])
#             break
#         elif input_list[input_index] > result_list[result_index]:
#             if result_index == len(result_list) - 1:
#                 result_list.appned(input_list[input_index])
#             pass
#
# print('\n'.join(map(str, input_list)))