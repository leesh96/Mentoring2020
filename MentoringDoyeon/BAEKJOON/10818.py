N = int(input())
# num_list = []
num_list = input().split()
# for i in range(N):
#     num_list[i] = int(num_list[i])
num_list = list(map(int, num_list))

# print(num_list)

Max = num_list[0]
for i in range(0, N-1):
    if Max < num_list[i+1]:
        Max = num_list[i+1]
    else:
        continue

Min = num_list[0]
for i in range(0, N-1):
    if Min > num_list[i+1]:
        Min = num_list[i+1]
    else:
        continue

print(Min, Max)