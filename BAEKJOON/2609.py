N, M = map(int, input().split())
if N < M:
    max_num = M
    min_num = N
elif N > M:
    max_num = M
    min_num = N
else:
    max_num = M
    min_num = max_num

for i in range(2, min_num+1): #minnm = 18
    if min_num % i == 0 and max_num % i == 0:
        result_1 = i

j = 1
while True:
    if (max_num * j) % min_num == 0:
        result_2 = max_num * j
        break
    else:
        j += 1

print(result_1)
print(result_2)