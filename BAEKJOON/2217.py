import sys

N = int(sys.stdin.readline())
rope_list = [int(sys.stdin.readline()) for _ in range(N)]

rope_list.sort(reverse=True)
result_list = []
for i in range(1, len(rope_list)+1):
    result_list.append(rope_list[i-1] * i)

print(max(result_list))
