num = []

for i in range(9):
    num.append(int(input()))

maximum = num[0]
index = 0

for i in range(1, 9):
    if maximum < num[i]:
        maximum = num[i]
        index = i

print(max(num))
print(index + 1)