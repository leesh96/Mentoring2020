import sys

N = int(input())

input_list = [int(sys.stdin.readline()) for _ in range(N)]

stack = []
result_list = []
i = 1
for target in input_list:
    while i <= target:
        stack.append(i)
        i += 1
        result_list.append('+')
    if stack[-1] > target:
        result_list.append('NO')
        break
    stack.pop()
    result_list.append('-')


if 'NO' not in result_list:
    for result in result_list:
        print(result)
else:
    print('NO')

