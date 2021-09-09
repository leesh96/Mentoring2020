import time

N = int(input())
san_list = list(map(int, input().split()))
M = int(input())
std_list = list(map(int, input().split()))
start = time.time()

for std in std_list:
    count = 0
    for num in san_list:
        if num == std:
            count += 1
        else:
            pass
    print(count, end=' ')

print(time.time()-start)

'''
while True:
    num_list = []
    num_list = input().split()
    if num_list == '':
        break
    num_list = list(map(int, num_list))
    print(num_list[0]+num_list[1])

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break'''
'''
for i in range(1, len(people_list)):
    for j in range(len(result_list)):
        if people_list[i][0] < result_list[j][0]:
            result_list.insert(j, people_list[i])
            break
        elif people_list[i][0] == result_list[j][0]:
            if people_list[i][2] == result_list[j][2] + 1:
                result_list.insert(j+1, people_list[i])
                break
        if j == len(result_list)-1:
            result_list.append(people_list[i])'''