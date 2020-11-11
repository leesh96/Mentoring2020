'''시간초과'''
# import sys
#
# K, N = map(int, sys.stdin.readline().rstrip().split())
# lan_list = [int(sys.stdin.readline()) for _ in range(K)]
#
# result = 0
# lan_result = [0 for _ in range(K)]
# for i in range(sum(lan_list) // N , 1,  -1):
#     result = i
#     for j in range(K):
#         lan_result[j] = lan_list[j] // i
#     if sum(lan_result) == N:
#         break
# print(result)

'''이분탐색'''
import sys

K, N = map(int, sys.stdin.readline().rstrip().split())
lan_list = [int(sys.stdin.readline()) for _ in range(K)]

lan_result = [0 for _ in range(K)]
start, end = 1, sum(lan_list) // N
while start <= end:
    mid = (start + end) // 2
    for i in range(K):
        lan_result[i] = lan_list[i] // mid

    if sum(lan_result) < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)