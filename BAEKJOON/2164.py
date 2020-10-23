N = int(input())
num_list = list(range(1, N+1))

for i in range(N-1):
    num_list.pop(0) #첫번째 수를 빼고
    num_list.append(num_list.pop(0)) #뺀 리스트에서 첫번째 수를 맨 뒤로
print(num_list[0])
#시간초과 ㅠ

