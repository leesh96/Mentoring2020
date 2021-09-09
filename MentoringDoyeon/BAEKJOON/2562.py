num_list = []
for i in range(9):
    num_list.append((int(input())))
# print(num_list)

Max = num_list[0]
Max_num = 1
for i in range(0, 8):
    if Max < num_list[i+1]:
        Max = num_list[i+1]
        Max_num = i+2
    else:
        continue

print(Max)
print(Max_num)

