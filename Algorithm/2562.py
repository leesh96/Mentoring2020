num = []

for i in range(9):
    num.append(int(input()))
    if i == 0:
        max = num[i]
        index = 0
    if num[i] > max:
        max = num[i]
        index = i

print(max, index + 1, sep='\n')