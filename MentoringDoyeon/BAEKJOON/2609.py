N, M = map(int, input().split())
if N < M:
    max_num = M
    min_num = N
elif N > M:
    max_num = M
    min_num = N
else:
    max_num == M
    min_num == N


for i in range(1, min_num+1): #2부터 min_num까지 체크
    if min_num % i == 0 and max_num % i == 0:
        result_1 = i

j = 1
while True: #max_num이 min_num으로 나누어 떨어지는 첫번째 수
    if (max_num * j) % min_num == 0:
        result_2 = max_num * j
        break
    else:
        j += 1

print(result_1)
print(result_2)