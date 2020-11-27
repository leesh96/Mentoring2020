import sys

N = int(sys.stdin.readline())
rope_list = [int(sys.stdin.readline()) for _ in range(N)]

rope_list.sort()
result_list = []
for i in range(len(rope_list)):
    result_list.append(rope_list[i] * (len(rope_list) - i))

print(max(result_list))
