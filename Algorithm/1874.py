import sys

size = int(sys.stdin.readline())
input_num = list(int(sys.stdin.readline()) for _ in range(size))

stack = []
print_op = []
count = 1
is_available = True

for num in input_num:
    while count <= num:
        stack.append(count)
        count += 1
        print_op.append("+")
    if stack[-1] == num:
        stack.pop()
        print_op.append("-")
    else:
        is_available = False

if is_available:
    for i in print_op:
        print(i)
else:
    print("NO")
