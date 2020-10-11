n = int(input())

for i in range(n):
    result = input()
    score = 0
    count = 0
    for j in list(result):
        if j == 'O':
            count += 1
            score += count
        elif j == 'X':
            count = 0
    print(score)