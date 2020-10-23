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
import sys

N = int(sys.stdin.readline()) #sys.stdin 이 더 빠름
input_list = []
for _ in range(N):
    input_list.append(int(sys.stdin.readline()))

result_list = []
result_list.append(input_list[0])
for input_index in range(1, N): # 인덱스로 num_list를 순서대로 꺼내기 위한 반복문. 최초 1개 추가했으니 1부터
    for result_index in range(len(result_list)): #result_list 요소를 탐색할 거니까 result_list 길이 만큼 반복
        '''result_list의 요소랑 하나씩 비교해서 만약 작은 수를 만나면 앞에 추가하고 아니면 작은 수를 만날 때 까지 반복.
        끝까지 작은 수를 못만나면 result_list중 가장 큰 수 이므로 맨 마지막에 추가'''
        if input_list[input_index] < result_list[result_index]:
            result_list.insert(result_index, input_list[input_index])
            break
        elif input_list[input_index] > result_list[result_index]:
            if result_index == len(result_list) - 1:
                result_list.appned(input_list[input_index])
            pass

print('\n'.join(map(str, result_list)))