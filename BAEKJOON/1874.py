import sys

N = int(input())

input_list = [int(sys.stdin.readline()) for _ in range(N)]

stack = []
result_list = []
i = 1
is_valid = True
for target in input_list:
    while i <= target:
        stack.append(i)
        i += 1
        result_list.append('+')
    if stack[-1] > target:
        is_valid = False
        break
    stack.pop()
    result_list.append('-')



if is_valid:
    for result in result_list:
        print(result)
else:
    print('NO')

