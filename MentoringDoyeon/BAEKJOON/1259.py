num_list, compare_list = [], []
while True:
    input_num = list(input())
    if input_num == ['0']:
        break
    else:
        num_list.append(input_num)

for i in range(len(num_list)):
    compare_list.append(list(reversed(num_list[i])))
for i in range(len(num_list)):
    if num_list[i] == compare_list[i] :
        print('yes')
    else:
        print('no')